#!/usr/bin/env python3
"""Scan a folder of Markdown or HTML content for retrieval-readiness signals.

Reports signals only. Judgment happens in the skill, not here.

Usage:
    python scan_content.py <folder> [--out scan.json] [--long-section 400]
"""

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path

GENERIC_HEADINGS = {
    "overview", "introduction", "intro", "details", "more info", "more information",
    "general", "notes", "misc", "miscellaneous", "other", "summary", "background",
    "getting started", "faq", "info",
}
DATE_PATTERN = re.compile(
    r"(last\s+(reviewed|updated|modified)|updated|reviewed)\s*[:\-]?\s*"
    r"(\d{4}-\d{2}-\d{2}|\w+\s+\d{1,2},?\s+\d{4})",
    re.IGNORECASE,
)
FRONTMATTER_DATE = re.compile(r"^(date|updated|last_reviewed|reviewed)\s*:", re.IGNORECASE | re.MULTILINE)
VAGUE_START = re.compile(r"^(it|this|that|these|those|they)\b", re.IGNORECASE)


class _HTMLToMarkdownish(HTMLParser):
    """Very small HTML to heading-aware text converter. Good enough for signals."""

    def __init__(self):
        super().__init__()
        self.lines = []
        self._heading = None
        self.images = 0
        self.images_without_alt = 0
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "nav", "footer"):
            self._skip += 1
        if re.fullmatch(r"h[1-6]", tag):
            self._heading = int(tag[1])
            self.lines.append("#" * self._heading + " ")
        if tag == "img":
            self.images += 1
            alt = dict(attrs).get("alt", "")
            if not alt or not alt.strip():
                self.images_without_alt += 1
        if tag in ("p", "li", "br", "tr"):
            self.lines.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "footer") and self._skip:
            self._skip -= 1
        if re.fullmatch(r"h[1-6]", tag):
            self._heading = None
            self.lines.append("\n")

    def handle_data(self, data):
        if not self._skip:
            self.lines.append(data)


def load_text(path: Path):
    raw = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix.lower() in (".html", ".htm"):
        parser = _HTMLToMarkdownish()
        parser.feed(raw)
        return "".join(parser.lines), parser.images, parser.images_without_alt, raw
    images = len(re.findall(r"!\[[^\]]*\]\([^)]+\)", raw))
    no_alt = len(re.findall(r"!\[\s*\]\([^)]+\)", raw))
    return raw, images, no_alt, raw


def split_sections(text: str):
    sections, current = [], {"heading": None, "level": 0, "body": []}
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m:
            sections.append(current)
            current = {"heading": m.group(2).strip(), "level": len(m.group(1)), "body": []}
        else:
            current["body"].append(line)
    sections.append(current)
    out = []
    for s in sections:
        body = " ".join(s["body"]).strip()
        if s["heading"] is None and not body:
            continue
        out.append({"heading": s["heading"], "level": s["level"], "body": body})
    return out


def passage_fingerprints(body: str, size: int = 40):
    words = re.findall(r"\w+", body.lower())
    if len(words) < size:
        return set()
    return {
        hashlib.md5(" ".join(words[i:i + size]).encode()).hexdigest()
        for i in range(0, len(words) - size + 1, size // 2)
    }


def scan(folder: Path, long_section: int):
    files = sorted(
        p for p in folder.rglob("*")
        if p.is_file() and p.suffix.lower() in (".md", ".markdown", ".mdx", ".html", ".htm", ".txt")
    )
    results, titles, prints = [], defaultdict(list), defaultdict(set)

    for path in files:
        text, images, no_alt, raw = load_text(path)
        sections = split_sections(text)
        headings = [s for s in sections if s["heading"]]
        rel = str(path.relative_to(folder))
        title = headings[0]["heading"] if headings else path.stem
        titles[title.lower().strip()].append(rel)

        long_sections, generic, vague_starts = [], [], []
        for s in sections:
            wc = len(s["body"].split())
            if wc > long_section:
                long_sections.append({"heading": s["heading"], "words": wc})
            if s["heading"] and s["heading"].lower().strip(" :") in GENERIC_HEADINGS:
                generic.append(s["heading"])
            if s["heading"] and VAGUE_START.match(s["body"]):
                vague_starts.append(s["heading"])
            for fp in passage_fingerprints(s["body"]):
                prints[fp].add(rel)

        word_count = len(text.split())
        results.append({
            "file": rel,
            "title": title,
            "words": word_count,
            "headings": len(headings),
            "has_review_date": bool(DATE_PATTERN.search(raw) or FRONTMATTER_DATE.search(raw)),
            "generic_headings": generic,
            "long_sections": long_sections,
            "sections_starting_with_pronoun": vague_starts,
            "images": images,
            "images_without_alt": no_alt,
            "image_heavy": images > 0 and word_count / max(images, 1) < 60,
        })

    duplicate_titles = {t: f for t, f in titles.items() if len(f) > 1}
    overlap = defaultdict(int)
    for fp, owners in prints.items():
        if len(owners) > 1:
            owners = sorted(owners)
            for i in range(len(owners)):
                for j in range(i + 1, len(owners)):
                    overlap[(owners[i], owners[j])] += 1
    near_duplicates = [
        {"files": list(pair), "shared_passages": n}
        for pair, n in sorted(overlap.items(), key=lambda kv: -kv[1]) if n >= 2
    ]

    summary = {
        "files_scanned": len(results),
        "missing_review_date": sum(1 for r in results if not r["has_review_date"]),
        "files_with_generic_headings": sum(1 for r in results if r["generic_headings"]),
        "files_with_long_sections": sum(1 for r in results if r["long_sections"]),
        "files_with_pronoun_openers": sum(1 for r in results if r["sections_starting_with_pronoun"]),
        "image_heavy_files": sum(1 for r in results if r["image_heavy"]),
        "images_without_alt": sum(r["images_without_alt"] for r in results),
        "duplicate_title_groups": len(duplicate_titles),
        "near_duplicate_pairs": len(near_duplicates),
    }
    return {
        "summary": summary,
        "duplicate_titles": duplicate_titles,
        "near_duplicates": near_duplicates[:50],
        "files": results,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("folder", type=Path)
    ap.add_argument("--out", type=Path, default=None, help="Write full JSON report here")
    ap.add_argument("--long-section", type=int, default=400, help="Word count that flags a section as long")
    args = ap.parse_args()

    if not args.folder.is_dir():
        sys.exit(f"Not a folder: {args.folder}")

    report = scan(args.folder, args.long_section)
    if args.out:
        args.out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    if report["duplicate_titles"]:
        print("\nDuplicate titles:")
        for t, files in report["duplicate_titles"].items():
            print(f"  {t}: {', '.join(files)}")
    if report["near_duplicates"]:
        print("\nNear-duplicate passages (top 10):")
        for d in report["near_duplicates"][:10]:
            print(f"  {d['files'][0]} <> {d['files'][1]} ({d['shared_passages']} shared passages)")


if __name__ == "__main__":
    main()

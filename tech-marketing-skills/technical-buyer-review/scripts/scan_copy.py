#!/usr/bin/env python3
"""
First-pass scanner for tech marketing copy.

Flags buzzwords, absolute claims, unattributed numbers, and common
AI-writing tells, with line numbers. It's a starting point for the
review, not a verdict: context decides whether a flag is a problem.

Usage:
    python scan_copy.py copy.txt
    python scan_copy.py copy.txt --json
    cat copy.txt | python scan_copy.py -
"""

import argparse
import json
import re
import sys

BUZZWORDS = [
    "seamless", "seamlessly", "robust", "cutting-edge", "cutting edge",
    "next-generation", "next-gen", "revolutionary", "revolutionize",
    "best-in-class", "world-class", "industry-leading", "leverage",
    "leverages", "leveraging", "unlock", "unlocks", "empower", "empowers",
    "game-changing", "game changer", "single pane of glass", "synergy",
    "holistic", "turnkey", "frictionless", "supercharge", "innovative",
    "state-of-the-art", "enterprise-grade", "mission-critical",
    "ai-powered", "ai-driven",
]

ABSOLUTES = [
    "100%", "zero downtime", "zero risk", "zero-trust", "never", "always",
    "guaranteed", "guarantee", "unhackable", "bulletproof", "eliminates",
    "eliminate", "completely", "every single",
]

AI_TELLS = [
    "delve", "in today's fast-paced", "in today’s fast-paced",
    "ever-evolving", "a testament to", "navigate the complexities",
    "at the end of the day", "look no further", "rest assured", "elevate",
    "tapestry", "harness the power", "leverage the power", "the power of ai", "it's not just", "it’s not just",
    "whether you're", "whether you’re",
]

# A number claim: percentages, multipliers, or "X times".
NUMBER_CLAIM = re.compile(
    r"\b\d+(?:\.\d+)?\s?(?:%|x\b|×|times\b)", re.IGNORECASE
)
# Words that suggest a source or method is nearby.
SOURCE_HINTS = re.compile(
    r"\b(according to|sourced?|study|studies|survey\w*|benchmark\w*|"
    r"measur\w*|based on|report\w*|case stud\w*|tested|compared to|"
    r"vs\.?|versus|against)\b",
    re.IGNORECASE,
)


def find_terms(line, terms):
    lowered = line.lower()
    hits = []
    for term in terms:
        pattern = r"(?<![\w-])" + re.escape(term.lower()) + r"(?![\w-])"
        if term.endswith("%"):
            pattern = re.escape(term.lower())
        if re.search(pattern, lowered):
            hits.append(term)
    return hits


def scan(text):
    lines = text.splitlines()
    findings = []
    for i, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        for term in find_terms(line, BUZZWORDS):
            findings.append({"line": i, "type": "buzzword", "match": term})
        for term in find_terms(line, ABSOLUTES):
            findings.append({"line": i, "type": "absolute", "match": term})
        for term in find_terms(line, AI_TELLS):
            findings.append({"line": i, "type": "ai_tell", "match": term})
        for m in NUMBER_CLAIM.finditer(line):
            if not SOURCE_HINTS.search(line):
                findings.append(
                    {"line": i, "type": "unattributed_number",
                     "match": m.group(0).strip()}
                )
    words = len(re.findall(r"\b\w+\b", text))
    return {"word_count": words, "findings": findings}


def print_report(result):
    findings = result["findings"]
    print(f"Words: {result['word_count']}  Flags: {len(findings)}")
    if not findings:
        print("No flags. Still read it as the buyer would.")
        return
    labels = {
        "buzzword": "Buzzword",
        "absolute": "Absolute claim",
        "ai_tell": "AI-writing tell",
        "unattributed_number": "Number with no visible source",
    }
    by_type = {}
    for f in findings:
        by_type.setdefault(f["type"], []).append(f)
    for kind in ["unattributed_number", "absolute", "buzzword", "ai_tell"]:
        items = by_type.get(kind)
        if not items:
            continue
        print(f"\n{labels[kind]} ({len(items)})")
        for f in items:
            print(f"  line {f['line']}: {f['match']}")
    per_100 = len(findings) / max(result["word_count"], 1) * 100
    print(f"\nFlag density: {per_100:.1f} per 100 words "
          "(above ~3 usually reads as fluff to technical buyers)")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("path", help="text file to scan, or - for stdin")
    parser.add_argument("--json", action="store_true", help="output JSON")
    args = parser.parse_args()

    if args.path == "-":
        text = sys.stdin.read()
    else:
        with open(args.path, encoding="utf-8") as fh:
            text = fh.read()

    result = scan(text)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)


if __name__ == "__main__":
    main()

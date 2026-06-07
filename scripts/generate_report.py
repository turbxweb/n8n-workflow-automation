#!/usr/bin/env python3
"""
Generate a human-readable Markdown report from the JSONL output of the workflow.

Usage:
    python3 scripts/generate_report.py <path-to-tickets.jsonl> <output.md>
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


def load_jsonl(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def render(tickets: list[dict]) -> str:
    total = len(tickets)
    by_cat = Counter(t.get("category", "Other") for t in tickets)
    by_sent = Counter(t.get("sentiment", "Neutral") for t in tickets)
    by_prio = Counter(t.get("priority", "Low") for t in tickets)
    errors = [t for t in tickets if t.get("ai_error")]

    lines: list[str] = []
    lines.append("# AI Ticket Triage — przykładowy raport")
    lines.append("")
    lines.append(f"**Liczba zgłoszeń:** {total}  ")
    lines.append(f"**Błędy analizy AI:** {len(errors)}")
    lines.append("")
    lines.append("## Podsumowanie")
    lines.append("")
    lines.append("### Kategorie")
    lines.append("")
    lines.append("| Kategoria | Liczba |")
    lines.append("|-----------|--------|")
    for cat in ("Recruitment", "Support", "Sales", "Other"):
        lines.append(f"| {cat} | {by_cat.get(cat, 0)} |")
    lines.append("")
    lines.append("### Sentyment")
    lines.append("")
    lines.append("| Sentyment | Liczba |")
    lines.append("|-----------|--------|")
    for s in ("Positive", "Neutral", "Negative"):
        lines.append(f"| {s} | {by_sent.get(s, 0)} |")
    lines.append("")
    lines.append("### Priorytet")
    lines.append("")
    lines.append("| Priorytet | Liczba |")
    lines.append("|-----------|--------|")
    for p in ("High", "Medium", "Low"):
        lines.append(f"| {p} | {by_prio.get(p, 0)} |")
    lines.append("")
    lines.append("## Zgłoszenia")
    lines.append("")
    lines.append("| # | Imię i nazwisko | Email | Kategoria | Sentyment | Priorytet | Fragment wiadomości |")
    lines.append("|---|-----------------|-------|-----------|-----------|-----------|---------------------|")
    for i, t in enumerate(tickets, 1):
        fullname = f"{t.get('name', '')} {t.get('surname', '')}".strip()
        msg = (t.get("message", "") or "").replace("\n", " ").replace("|", "\\|")
        if len(msg) > 80:
            msg = msg[:77] + "..."
        lines.append(
            f"| {i} | {fullname} | {t.get('email', '')} "
            f"| {t.get('category', '')} | {t.get('sentiment', '')} "
            f"| {t.get('priority', '')} | {msg} |"
        )
    lines.append("")

    high = [t for t in tickets if t.get("priority") == "High"]
    if high:
        lines.append("## Zgłoszenia HIGH (wymagają natychmiastowej reakcji)")
        lines.append("")
        for t in high:
            fullname = f"{t.get('name', '')} {t.get('surname', '')}".strip()
            lines.append(f"###  {fullname} — {t.get('category', '')}")
            lines.append("")
            lines.append(f"- **Email:** {t.get('email', '')}")
            lines.append(f"- **Sentyment:** {t.get('sentiment', '')}")
            lines.append(f"- **Uzasadnienie AI:** {t.get('reasoning', '—')}")
            lines.append("")
            lines.append("**Treść:**")
            lines.append("")
            lines.append(f"> {t.get('message', '')}")
            lines.append("")

    if errors:
        lines.append("## Błędy analizy AI")
        lines.append("")
        for t in errors:
            lines.append(f"- {t.get('email', '?')}: `{t.get('ai_error')}`")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: generate_report.py <tickets.jsonl> <output.md>", file=sys.stderr)
        return 2
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    if not src.is_file():
        print(f"input not found: {src}", file=sys.stderr)
        return 1
    tickets = load_jsonl(src)
    dst.write_text(render(tickets), encoding="utf-8")
    print(f"wrote {dst} ({len(tickets)} tickets)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

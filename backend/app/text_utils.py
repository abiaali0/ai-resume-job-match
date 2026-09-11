from __future__ import annotations

import re

STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has",
    "have", "in", "is", "it", "of", "on", "or", "our", "that", "the", "this",
    "to", "we", "will", "with", "you", "your"
}

CANONICAL_TERMS = {
    "javascript": {"javascript", "js"},
    "typescript": {"typescript", "ts"},
    "postgresql": {"postgresql", "postgres"},
    "machine learning": {"machine learning", "ml"},
    "artificial intelligence": {"artificial intelligence", "ai"},
    "continuous integration": {"continuous integration", "ci"},
    "continuous deployment": {"continuous deployment", "cd"},
}


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.lower()).strip()


def extract_keywords(value: str) -> set[str]:
    normalized = normalize_text(value)
    keywords: set[str] = set()

    for canonical, variants in CANONICAL_TERMS.items():
        if any(variant in normalized for variant in variants):
            keywords.add(canonical)

    words = re.findall(r"[a-z][a-z0-9+#.-]{2,}", normalized)

    for word in words:
        cleaned = word.strip(".-")
        if cleaned and cleaned not in STOP_WORDS:
            keywords.add(cleaned)

    return keywords

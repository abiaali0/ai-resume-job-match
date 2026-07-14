from __future__ import annotations

from app.text_utils import extract_keywords

HIGH_VALUE_TERMS = {
    "python", "java", "javascript", "typescript", "react", "fastapi",
    "node.js", "docker", "kubernetes", "aws", "gcp", "azure",
    "postgresql", "mongodb", "redis", "sql", "machine learning",
    "artificial intelligence", "pytorch", "tensorflow", "git"
}


def calculate_match(
    resume_text: str,
    job_description: str,
) -> dict[str, object]:
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)

    if not job_keywords:
        return {
            "match_score": 0.0,
            "matched_keywords": [],
            "missing_keywords": [],
            "suggestions": ["The job description did not contain enough analyzable content."],
        }

    matched = resume_keywords & job_keywords
    missing = job_keywords - resume_keywords

    weighted_total = sum(2 if term in HIGH_VALUE_TERMS else 1 for term in job_keywords)
    weighted_match = sum(2 if term in HIGH_VALUE_TERMS else 1 for term in matched)

    score = round((weighted_match / weighted_total) * 100, 1)

    missing_priority = sorted(
        missing,
        key=lambda term: (term not in HIGH_VALUE_TERMS, term),
    )[:10]

    suggestions = [
        f"Add evidence of experience with {term} if you have genuinely used it."
        for term in missing_priority
    ]

    if not suggestions:
        suggestions.append(
            "Your resume covers the main detected requirements. Strengthen it with measurable outcomes."
        )

    return {
        "match_score": score,
        "matched_keywords": sorted(matched),
        "missing_keywords": sorted(missing),
        "suggestions": suggestions,
    }

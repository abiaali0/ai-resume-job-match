from app.matcher import calculate_match


def test_match_detects_overlap_and_missing_terms() -> None:
    result = calculate_match(
        "Python developer with FastAPI, Docker and PostgreSQL.",
        "Seeking Python, FastAPI, Docker, PostgreSQL and Redis experience.",
    )

    assert result["match_score"] > 0
    assert "python" in result["matched_keywords"]
    assert "redis" in result["missing_keywords"]


def test_complete_match_scores_full() -> None:
    result = calculate_match(
        "Python FastAPI Docker Redis PostgreSQL",
        "Python FastAPI Docker Redis PostgreSQL",
    )

    assert result["match_score"] == 100.0
    assert result["missing_keywords"] == []

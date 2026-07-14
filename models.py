from pydantic import BaseModel, Field


class MatchRequest(BaseModel):
    resume_text: str = Field(min_length=20, max_length=30_000)
    job_description: str = Field(min_length=20, max_length=30_000)


class MatchResponse(BaseModel):
    match_score: float
    matched_keywords: list[str]
    missing_keywords: list[str]
    suggestions: list[str]

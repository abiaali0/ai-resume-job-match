from fastapi import FastAPI

from app.matcher import calculate_match
from app.models import MatchRequest, MatchResponse

app = FastAPI(
    title="AI-Powered Resume & Job Match Platform",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/match", response_model=MatchResponse)
def match_resume(request: MatchRequest) -> MatchResponse:
    result = calculate_match(
        request.resume_text,
        request.job_description,
    )
    return MatchResponse(**result)

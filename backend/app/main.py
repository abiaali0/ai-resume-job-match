from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.matcher import calculate_match
from app.models import MatchRequest, MatchResponse

app = FastAPI(
    title="AI-Powered Resume & Job Match Platform",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

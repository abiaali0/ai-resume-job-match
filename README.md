# AI-Powered Resume & Job Match Platform

A full-stack application that compares résumé content with job descriptions, calculates a transparent match score, identifies missing keywords, and generates targeted improvement suggestions.

> **Original project year:** 2023 
> **Public repository reconstruction:** July 2026  
> **Status:** Active portfolio reconstruction using verified, original work only

## Current Public Implementation

This repository currently includes:

- FastAPI backend
- Resume and job-description text processing
- Keyword extraction
- Weighted match scoring
- Missing-keyword analysis
- Improvement suggestions
- React frontend
- REST API integration
- Automated backend tests
- Docker support
- GitHub Actions continuous integration

The résumé also references semantic search, resume parsing, authentication, saved application tracking, PostgreSQL, OpenAI API, NLP, and Tailwind CSS. Those features should only be added publicly after they are implemented and verified.

## How It Works

```text
Resume text
    +
Job description
    ↓
Text normalization
    ↓
Keyword extraction
    ↓
Skill overlap analysis
    ↓
Weighted match score
    ↓
Missing-keyword report
    ↓
Targeted suggestions
```

## API

### Health check

```http
GET /health
```

### Analyze a resume against a job description

```http
POST /match
Content-Type: application/json
```

Example request:

```json
{
  "resume_text": "Python developer with FastAPI, PostgreSQL and Docker experience.",
  "job_description": "Seeking a backend engineer with Python, FastAPI, Docker, Redis and PostgreSQL."
}
```

Example response:

```json
{
  "match_score": 80.0,
  "matched_keywords": ["docker", "fastapi", "postgresql", "python"],
  "missing_keywords": ["redis"],
  "suggestions": [
    "Add evidence of experience with Redis if you have genuinely used it."
  ]
}
```

## Run Locally

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Run Backend Tests

```bash
cd backend
pytest
```

## Project Structure

```text
ai-resume-job-match/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── matcher.py
│   │   ├── models.py
│   │   └── text_utils.py
│   ├── tests/
│   │   └── test_matcher.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── .github/
│   └── workflows/
│       └── ci.yml
├── docker-compose.yml
└── README.md
```

## Development Timeline

- **2026:** Original project work
- **July 2026:** Public portfolio reconstruction and documentation

The résumé does not state exact original months, so this repository does not claim a more specific timeline.

## Accuracy Note

This public version uses transparent, deterministic scoring. It does not claim to use an LLM, semantic embeddings, authentication, or saved application tracking until those features are actually implemented and verified.

Do not upload private resumes, employer data, credentials, or material you do not own.

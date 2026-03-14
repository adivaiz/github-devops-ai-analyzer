from fastapi import APIRouter, Request
import json
from backend.ai_analyzer import analyze_event, summarize_event
from backend.ai_service import get_ai_insight

router = APIRouter()

@router.post("/github-event")
async def github_event(request: Request):
    payload = await request.json()

    # Save the raw event to a file
    with open("data/events.json", "a") as f:
        f.write(json.dumps(payload) + "\n")

    # Prepare a clean summary of the event
    summary = summarize_event(payload)

    # Rule-based analysis
    insight = analyze_event(payload)

    # AI-based placeholder analysis
    ai_insight = get_ai_insight(summary)

    print("Event Summary:", summary)
    print("Rule-Based Insight:", insight)
    print("AI Service Insight:", ai_insight)

    return {
        "status": "event received",
        "summary": summary,
        "insight": insight,
        "ai_insight": ai_insight
    }

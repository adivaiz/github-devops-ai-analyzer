from fastapi import APIRouter, Body
import json
from backend.ai_analyzer import analyze_event, summarize_event
from backend.ai_service import get_ai_insight

router = APIRouter()

@router.post("/github-event")
async def github_event(payload: dict = Body(...)):

    # Save event
    with open("data/events.json", "a") as f:
        f.write(json.dumps(payload) + "\n")

    summary = summarize_event(payload)
    insight = analyze_event(payload)
    ai_insight = get_ai_insight(summary)

    print("Event Summary:", summary)
    print("Rule-Based Insight:", insight)
    print("AI Insight:", ai_insight)

    return {
        "status": "event received",
        "summary": summary,
        "insight": insight,
        "ai_insight": ai_insight
    }
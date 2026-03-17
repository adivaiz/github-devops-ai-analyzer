from fastapi import APIRouter, Body
import json
from datetime import datetime, timezone

from backend.ai_analyzer import analyze_event, summarize_event
from backend.ai_service import get_ai_insight

router = APIRouter()


@router.post("/github-event")
async def github_event(payload: dict = Body(...)):
    # Analyze event
    summary = summarize_event(payload)
    insight = analyze_event(payload)
    ai_insight = get_ai_insight(summary)

    # Build event record
    event_record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "summary": summary,
        "insight": insight,
        "ai_insight": ai_insight,
        "raw_event": payload
    }

    # Save event
    with open("data/events.json", "a") as f:
        f.write(json.dumps(event_record) + "\n")

    print("Event Summary:", summary)
    print("Rule-Based Insight:", insight)
    print("AI Insight:", ai_insight)

    return {
        "status": "event received",
        "summary": summary,
        "insight": insight,
        "ai_insight": ai_insight
    }
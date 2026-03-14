from fastapi import APIRouter, Request
import json
from backend.ai_analyzer import analyze_event, summarize_event

router = APIRouter()

@router.post("/github-event")
async def github_event(request: Request):
    payload = await request.json()

    # Save the raw event to a file
    with open("data/events.json", "a") as f:
        f.write(json.dumps(payload) + "\n")

    # Prepare a clean summary of the event
    summary = summarize_event(payload)

    # Analyze the event
    insight = analyze_event(payload)

    print("Event Summary:", summary)
    print("AI Insight:", insight)

    return {
        "status": "event received",
        "summary": summary,
        "insight": insight
    }

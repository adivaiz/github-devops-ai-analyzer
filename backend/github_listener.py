from fastapi import APIRouter, Request
import json
from backend.ai_analyzer import analyze_event

router = APIRouter()

@router.post("/github-event")
async def github_event(request: Request):

    payload = await request.json()

    # Save the event to a file
    with open("data/events.json", "a") as f:
        f.write(json.dumps(payload) + "\n")

    # Analyze the event
    insight = analyze_event(payload)

    print("AI Insight:", insight)

    return {
        "status": "event received",
        "insight": insight
    }

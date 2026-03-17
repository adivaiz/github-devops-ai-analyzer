from fastapi import APIRouter, Body
import json
from datetime import datetime, timezone
from fastapi.responses import HTMLResponse
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
@router.get("/events")
async def get_events():
    events = []

    try:
        with open("data/events.json", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    events.append(json.loads(line))
    except FileNotFoundError:
        return []

    events.reverse()
    return events
@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    events = []

    try:
        with open("data/events.json", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    events.append(json.loads(line))
    except FileNotFoundError:
        events = []

    events.reverse()

    html = """
    <html>
    <head>
        <title>GitHub DevOps AI Dashboard</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                padding: 30px;
            }
            h1 {
                color: #222;
            }
            .card {
                background: white;
                padding: 16px;
                margin-bottom: 16px;
                border-radius: 12px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            }
            .label {
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h1>GitHub DevOps AI Dashboard</h1>
    """

    for event in events:
        summary = event.get("summary", {})
        html += f"""
        <div class="card">
            <div><span class="label">Time:</span> {event.get("timestamp", "N/A")}</div>
            <div><span class="label">Event Type:</span> {summary.get("event_type", "N/A")}</div>
            <div><span class="label">Repository:</span> {summary.get("repository", "N/A")}</div>
            <div><span class="label">Sender:</span> {summary.get("sender", "N/A")}</div>
            <div><span class="label">Action:</span> {summary.get("action", "N/A")}</div>
            <div><span class="label">Rule-Based Insight:</span> {event.get("insight", "N/A")}</div>
            <div><span class="label">AI Insight:</span> {event.get("ai_insight", "N/A")}</div>
        </div>
        """

    html += """
    </body>
    </html>
    """

    return html
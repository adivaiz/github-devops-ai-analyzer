from fastapi import APIRouter, Request
import json

router = APIRouter()

@router.post("/github-event")
async def github_event(request: Request):
    payload = await request.json()

    # שמירת האירוע
    with open("events.json", "a") as f:
        f.write(json.dumps(payload) + "\n")

    return {"status": "event received"}

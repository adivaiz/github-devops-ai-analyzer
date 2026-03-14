import os
from dotenv import load_dotenv

load_dotenv()


def get_ai_insight(summary):
    """
    Placeholder for real AI integration.
    For now, this function builds a prompt-like text
    from the event summary and returns a mock AI response.
    """

    event_type = summary.get("event_type", "unknown")
    repository = summary.get("repository", "unknown")
    sender = summary.get("sender", "unknown")
    action = summary.get("action", "unknown")

    prompt = (
        f"Analyze this GitHub event:\n"
        f"Event type: {event_type}\n"
        f"Repository: {repository}\n"
        f"Sender: {sender}\n"
        f"Action: {action}\n"
        f"Summary: {summary}\n"
    )

    return f"Mock AI insight based on event '{event_type}' in repository '{repository}'."

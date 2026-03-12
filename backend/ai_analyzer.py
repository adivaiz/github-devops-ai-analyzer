
"""
AI Analyzer Module

This module analyzes GitHub events received by the system.
In the future it will connect to an AI model, but for now it performs
simple rule-based analysis.
"""
def analyze_event(event):
    """
    Analyze a GitHub event and return a simple insight.
    """

    # Identify the type of GitHub event
    event_type = event.get("action", "unknown")

    # Example insights
    if event_type == "opened":
        return "A new pull request was opened."

    if event_type == "closed":
        return "A pull request was closed."

    if event_type == "push":
        return "Code was pushed to the repository."

    # Default message
    return "Event received but no analysis rule matched."

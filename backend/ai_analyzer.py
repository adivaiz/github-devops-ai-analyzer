"""
AI Analyzer Module

This module analyzes GitHub events received by the system.
For now, it performs simple rule-based analysis based on
common GitHub event types and actions.
"""


def analyze_event(event):
    """
    Analyze a GitHub event and return an insight string.
    """

    action = event.get("action", "unknown")

    # Detect push events
    if "commits" in event:
        commit_count = len(event.get("commits", []))

        if commit_count == 0:
            return "A push event was received with no commits."

        if commit_count == 1:
            return "A single commit was pushed to the repository."

        if commit_count > 1:
            return f"{commit_count} commits were pushed to the repository."

    # Detect pull request related actions
    if "pull_request" in event:
        if action == "opened":
            return "A new pull request was opened."

        if action == "closed":
            return "A pull request was closed."

        if action == "reopened":
            return "A pull request was reopened."

        return f"A pull request event was received with action: {action}."

    # Detect branch or tag creation
    if action == "created":
        return "A new branch or tag was created."

    # Detect branch or tag deletion
    if action == "deleted":
        return "A branch or tag was deleted."

    # Generic opened / closed fallback
    if action == "opened":
        return "An item was opened in the repository."

    if action == "closed":
        return "An item was closed in the repository."

    # Default fallback
    return f"Event received with unrecognized action: {action}."

"""
AI Analyzer Module

This module prepares GitHub event data for analysis.
For now, it returns a structured summary and a simple fallback insight.
Later, the summary can be sent to a real AI model for deeper analysis.
"""


def summarize_event(event):
    """
    Extract the most important fields from a GitHub event payload.
    Returns a clean summary dictionary.
    """

    summary = {
        "action": event.get("action", "unknown"),
        "repository": event.get("repository", {}).get("full_name", "unknown"),
        "sender": event.get("sender", {}).get("login", "unknown"),
        "event_type": "unknown"
    }

    # Push event
    if "commits" in event:
        summary["event_type"] = "push"
        summary["commit_count"] = len(event.get("commits", []))
        summary["ref"] = event.get("ref", "unknown")

    # Pull request event
    elif "pull_request" in event:
        pr = event.get("pull_request", {})
        summary["event_type"] = "pull_request"
        summary["pr_title"] = pr.get("title", "unknown")
        summary["pr_state"] = pr.get("state", "unknown")
        summary["pr_number"] = pr.get("number", "unknown")

    # Workflow run event
    elif "workflow_run" in event:
        workflow = event.get("workflow_run", {})
        summary["event_type"] = "workflow_run"
        summary["workflow_name"] = workflow.get("name", "unknown")
        summary["workflow_status"] = workflow.get("status", "unknown")
        summary["workflow_conclusion"] = workflow.get("conclusion", "unknown")

    return summary


def analyze_event(event):
    """
    Analyze a GitHub event and return a simple insight.
    This is a fallback layer until a real AI model is connected.
    """

    summary = summarize_event(event)

    if summary["event_type"] == "push":
        commit_count = summary.get("commit_count", 0)

        if commit_count == 0:
            return "Push event detected, but no commits were included."

        if commit_count == 1:
            return "Push event detected with one commit."

        return f"Push event detected with {commit_count} commits."

    if summary["event_type"] == "pull_request":
        action = summary.get("action", "unknown")
        title = summary.get("pr_title", "unknown")

        if action == "opened":
            return f"Pull request opened: {title}"

        if action == "closed":
            return f"Pull request closed: {title}"

        if action == "reopened":
            return f"Pull request reopened: {title}"

        return f"Pull request event detected with action: {action}"

    if summary["event_type"] == "workflow_run":
        conclusion = summary.get("workflow_conclusion", "unknown")
        workflow_name = summary.get("workflow_name", "unknown")

        if conclusion == "success":
            return f"Workflow '{workflow_name}' completed successfully."

        if conclusion == "failure":
            return f"Workflow '{workflow_name}' failed."

        return f"Workflow '{workflow_name}' event detected with conclusion: {conclusion}"

    return f"Event detected with action: {summary.get('action', 'unknown')}"

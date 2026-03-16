import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")
HF_MODEL_ID = os.getenv("HF_MODEL_ID", "openai/gpt-oss-120b:fastest")


def get_ai_insight(summary):
    """
    Send the GitHub event summary to a Hugging Face chat model
    and return a short AI-generated DevOps insight.
    """

    if not HF_API_KEY:
        return "AI service not configured."

    try:
        client = InferenceClient(api_key=HF_API_KEY)

        completion = client.chat.completions.create(
            model=HF_MODEL_ID,
            messages=[
                {
                    "role": "system",
                    "content": "You are a DevOps incident analysis assistant. Return one short practical insight."
                },
                {
                    "role": "user",
                    "content": f"Analyze this GitHub event summary:\n{summary}"
                }
            ],
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        return f"AI error: {str(e)}"
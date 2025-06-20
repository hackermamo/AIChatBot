from .config import GEMINI_API_KEY
from tenacity import retry, stop_after_attempt, wait_fixed
import httpx

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def generate_title(query: str) -> str:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}

    prompt = (
        f"Write a professional and engaging tweet (max 120 characters) "
        f"about this topic: '{query}'. "
        f"It should be insightful, include emojis, and relevant hashtags. "
        f"Use a tone similar to tech or AI thought leaders. "
        f"Keep it informative, conversational, and suitable for Twitter."
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = httpx.post(url, json=payload, headers=headers, timeout=10)
    response.raise_for_status()

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]

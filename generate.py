import httpx
import os

API_KEY ="AIzaSyBL4Vxyq2cVg3MRHNjIemYLmy7UeMiYiGg"  # Or replace with your actual API key string here

def generate_title(prompt: str) -> str:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = httpx.post(url, headers=headers, json=data)
    
    try:
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except httpx.HTTPStatusError as e:
        print(f"HTTP error: {e.response.status_code} - {e.response.text}")
        raise
    except KeyError:
        print("Unexpected response format:", response.text)
        raise

if __name__ == "__main__":
    user_input = input("Enter your prompt for title generation: ")
    try:
        result = generate_title(user_input)
        print("\nGenerated Title:")
        print(result)
    except Exception as e:
        print("\nSomething went wrong:", e)

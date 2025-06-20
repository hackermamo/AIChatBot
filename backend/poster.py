from .config import LITERARY_API_KEY, FACEBOOK_API_KEY, FACEBOOK_PAGE_ID
import httpx

# ✅ Send tweet to literary (Twitter clone) with username
def post_to_literary(title: str, username: str = "maman"):
    url = "https://twitterclone-server-2xz2.onrender.com/post_tweet"
    headers = {
        "Accept": "application/json",  # Added
        "Content-Type": "application/json",
        "api-key": LITERARY_API_KEY
    }
    payload = {
        "username": username,
        "text": title
    }

    try:
        response = httpx.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()

        print("✅ Literary response:", response.status_code, response.json())
        return response.json()

    except httpx.HTTPStatusError as e:
        print("❌ HTTP error:", e.response.status_code, e.response.text)
        raise
    except Exception as e:
        print("❌ Other error:", str(e))
        raise

# ✅ Post to Facebook clone
def post_to_facebook_clone(title: str):
    url = f"https://graph.facebook.com/{FACEBOOK_PAGE_ID}/feed"
    payload = {
        "message": title,
        "access_token": FACEBOOK_API_KEY
    }

    try:
        response = httpx.post(url, data=payload, timeout=10)
        response.raise_for_status()
        print("✅ Facebook response:", response.status_code, response.json())
        return response.json()

    except httpx.HTTPStatusError as e:
        print("❌ HTTP error:", e.response.status_code, e.response.text)
        raise
    except Exception as e:
        print("❌ Other error:", str(e))
        raise

# ✅ Post to platforms (Twitter + Facebook)
def post_to_platforms(title: str, platforms: list, username: str = "maman"):
    results = {}
    for platform in platforms:
        try:
            if platform == "Twitter":
                results["Twitter"] = post_to_literary(title, username=username)
            elif platform == "Facebook":
                results["Facebook"] = post_to_facebook_clone(title)
        except Exception as e:
            results[platform] = {"error": str(e)}
    return results

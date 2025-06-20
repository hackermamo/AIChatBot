import json
from datetime import datetime
from pathlib import Path

# ✅ Use raw string or Path for Windows paths
HISTORY_FILE = Path(r"C:\Users\HP\Desktop\ai-title-agent\backend\history.jsonl")
HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)

def log_history(
    query: str,
    title: str,
    platforms: list[str],
    username: str = None,
    status: str = "success",
    error_message: str = None
) -> None:
    entry = {
        "timestamp": datetime.now().isoformat(),
        "query": query,
        "title": title,
        "platforms": platforms,
        "username": username,
        "status": status,
        "error": error_message
    }

    # Remove None fields for cleanliness
    entry = {k: v for k, v in entry.items() if v is not None}

    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

def read_history() -> list[dict]:
    if not HISTORY_FILE.exists():
        return []
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]

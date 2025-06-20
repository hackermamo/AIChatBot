from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .title_generator import generate_title
from .poster import post_to_platforms
from .logger import log_history, read_history
import asyncio
import sys
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Mount frontend static folder
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# ✅ Serve index.html
@app.get("/")
def serve_home():
    return FileResponse("frontend/index.html")

@app.post("/generate-title")
async def generate(request: Request):
    try:
        data = await request.json()
    except Exception:
        return {"error": "Invalid JSON received"}
    
    query = data.get("query")
    if not query:
        return {"error": "Missing 'query' in request"}
    
    title = generate_title(query)
    return {"title": title}


@app.post("/post")
async def post(request: Request):
    data = await request.json()
    title = data.get("title")
    platforms = data.get("platforms", [])
    result = post_to_platforms(title, platforms)
    return {"status": "posted", "result": result}

@app.get("/history")
def history():
    return {"history": read_history()}




if __name__ == "__main__":
    try:
        import uvicorn
        uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
    except asyncio.CancelledError:
        # Suppress reload cancellation error
        pass
    except KeyboardInterrupt:
        print("Server interrupted.", file=sys.stderr)

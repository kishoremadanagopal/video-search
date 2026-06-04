from fastapi import FastAPI

app = FastAPI(title="video-search")


@app.get("/health")
def health():
    return {"status": "ok"}

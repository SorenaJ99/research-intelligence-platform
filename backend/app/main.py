from fastapi import FastAPI

app = FastAPI(
    title="Research Intelligence Platform",
    version="0.1.0"
)


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/about")
def about():
    return {
        "project": "Research Intelligence Platform",
        "phase": "Backend Foundation"
    }
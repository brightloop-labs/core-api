from fastapi import FastAPI

app = FastAPI(title="core-api")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}
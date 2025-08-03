from fastapi import FastAPI
from app.routers import orders

app = FastAPI(title="core-api")
app.include_router(orders.router)


@app.get("/healthz")
def healthz():
    return {"status": "ok"}
from fastapi import FastAPI
from app.routers import orders, refunds
from app.middleware.rate_limit import RateLimitMiddleware
from app import webhooks

app = FastAPI(title="core-api")
app.add_middleware(RateLimitMiddleware)
app.include_router(orders.router)
app.include_router(refunds.router)
app.include_router(webhooks.router)


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/health/live")
def live():
    return {"status": "live"}


@app.get("/health/ready")
def ready():
    return {"status": "ready"}
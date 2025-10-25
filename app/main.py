from fastapi import FastAPI
from app.routers import orders
from app.middleware.rate_limit import RateLimitMiddleware

app = FastAPI(title="core-api")
app.add_middleware(RateLimitMiddleware)
app.include_router(orders.router)


@app.get("/healthz")
def healthz():
    return {"status": "ok"}
import hashlib
import hmac
import os
from fastapi import APIRouter, Header, HTTPException, Request

router = APIRouter(prefix="/webhooks", tags=["webhooks"])
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "change-me")


def _verify_signature(body: bytes, signature: str) -> bool:
    expected = hmac.new(WEBHOOK_SECRET.encode(), body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)


@router.post("/payment-events")
async def payment_events(request: Request, x_signature: str = Header(...)):
    body = await request.body()
    if not _verify_signature(body, x_signature):
        raise HTTPException(status_code=401, detail="Invalid signature")
    return {"received": True}
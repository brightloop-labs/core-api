from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/refunds", tags=["refunds"])

_refunds_db = {}
_next_id = 1


class RefundCreate(BaseModel):
    order_id: int
    amount: float
    reason: str | None = None


class RefundOut(RefundCreate):
    id: int
    status: str


@router.post("/", response_model=RefundOut)
def create_refund(refund: RefundCreate):
    global _next_id
    record = RefundOut(id=_next_id, status="processed", **refund.dict())
    _refunds_db[_next_id] = record
    _next_id += 1
    return record


@router.get("/{refund_id}", response_model=RefundOut)
def get_refund(refund_id: int):
    if refund_id not in _refunds_db:
        raise HTTPException(status_code=404, detail="Refund not found")
    return _refunds_db[refund_id]
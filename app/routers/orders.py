from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/orders", tags=["orders"])

_orders_db = {}
_next_id = 1


class OrderCreate(BaseModel):
    customer_email: str
    total_amount: float


class OrderOut(OrderCreate):
    id: int
    status: str


@router.get("/", response_model=list[OrderOut])
def list_orders():
    return list(_orders_db.values())


@router.post("/", response_model=OrderOut)
def create_order(order: OrderCreate):
    global _next_id
    record = OrderOut(id=_next_id, status="pending", **order.dict())
    _orders_db[_next_id] = record
    _next_id += 1
    return record


@router.get("/{order_id}", response_model=OrderOut)
def get_order(order_id: int):
    if order_id not in _orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    return _orders_db[order_id]
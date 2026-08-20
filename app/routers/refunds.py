from fastapi import APIRouter

router = APIRouter(prefix="/refunds", tags=["refunds"])


@router.post("/")
def create_refund():
    # TODO: implement refund processing
    return {"status": "not_implemented"}
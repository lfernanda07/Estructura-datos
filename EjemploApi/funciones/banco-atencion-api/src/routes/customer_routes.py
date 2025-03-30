from fastapi import APIRouter, HTTPException
from src.services.queue_service import QueueService

router = APIRouter()
queue_service = QueueService()

@router.post("/enqueue/")
def enqueue_customer(customer_data: dict):
    try:
        queue_service.add_customer(customer_data)
        return {"message": "Customer added to the queue"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/next/")
def get_next_customer():
    try:
        next_customer = queue_service.get_next_customer()
        if next_customer:
            return {"next_customer": next_customer}
        else:
            raise HTTPException(status_code=404, detail="No customers in the queue")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/pending/")
def list_pending_customers():
    try:
        pending_customers = queue_service.list_pending_customers()
        return {"pending_customers": pending_customers}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
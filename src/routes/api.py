from fastapi import APIRouter
from src.endpoints import disease_prediction_endp

router = APIRouter()
router.include_router(disease_prediction_endp.router)




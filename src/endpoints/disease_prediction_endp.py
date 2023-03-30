from fastapi import HTTPException, APIRouter
from src.database.disease_prediction import predictDisease
from src.database.filter_user_symptoms import filterUserSymptom
from src.models.symptoms_model import Symptoms

router = APIRouter(
    prefix="/api/predict_disease",
    tags=["predict_disease"],
    responses={404: {"description": "Not found"}},
)


@router.post("/getdisease")
def get_disease(data : Symptoms):
    print(data.symptoms)
    result = filterUserSymptom(data.symptoms)
    response = predictDisease(result)
    return {"Disease":response}



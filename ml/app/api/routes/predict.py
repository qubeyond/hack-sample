from fastapi import APIRouter, Depends

from app.api.deps import get_predictor
from app.api.schemas.predict import PredictRequest, PredictResponse
from app.inference.predictor import Predictor

router = APIRouter(tags=["predict"])


@router.post("/predict", response_model=PredictResponse)
def run_predict(payload: PredictRequest, predictor: Predictor = Depends(get_predictor)):
    result = predictor.predict(payload.features)
    return PredictResponse(prediction=result)

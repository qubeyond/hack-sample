from functools import lru_cache

from app.config import settings
from app.inference.predictor import Predictor


@lru_cache
def get_predictor() -> Predictor:
    return Predictor(model_path=settings.model_path)

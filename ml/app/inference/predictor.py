class Predictor:
    def __init__(self, model_path: str | None = None):
        self.model_path = model_path
        self.model = self._load(model_path) if model_path else None

    def _load(self, path: str):
        return None

    def predict(self, features: list[float]) -> float:
        return sum(features) / len(features) if features else 0.0

# ml

No `domain` layer here — that's for backend's entity-heavy CRUD, this service is just "load a model + run it".

## Layout
- `config.py` — `Settings` (pydantic-settings), same pattern as backend. `deps.py` reads it and passes plain values into constructors — a module like `inference/predictor.py` never calls `os.getenv` itself.
- `api/` — FastAPI routers + `deps.py` (dependency wiring, same pattern as backend).
- `api/schemas/` — Pydantic request/response DTOs, one per endpoint. Every endpoint has one, including `/health`. Lives under `api/` because nothing outside `api/` should import it.
- `inference/` — the one capability this template ships: `predictor.py` loads weights (from `MODEL_PATH`) and runs prediction.

## Adding a new capability (RAG, an agent, a second model, etc.)
- Add a sibling module next to `inference/` (e.g. `rag/`, `agents/`) with its own load + run logic. Don't nest it inside `inference/`.
- Wire it into `api/deps.py` the same way `get_predictor` is wired, and give it its own route + schema.
- Don't extract a shared base class/interface until there are 2+ real implementations that actually need one — one predictor + one RAG module can stay unrelated.

## Tests
- Functional style: plain functions, no test classes. One `client` fixture in `tests/conftest.py`, reused by every test file.
- Hit the actual HTTP routes through `client`, assert on status code + JSON body.
- To add a test: drop a new `tests/test_<thing>.py`, write `def test_...(client): ...`, copy the pattern from `tests/test_predict.py`.

## Commands
- Package manager: `uv`. Run: `uv run uvicorn app.main:app --reload` (installs deps automatically).
- Lint + format: `uv run ruff format . && uv run ruff check .`. Config extends root `ruff.toml`.
- Tests: `uv run pytest`.

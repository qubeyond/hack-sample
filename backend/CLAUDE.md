# backend

FastAPI service. Layers: `domain -> services -> infra -> api`. Inner layers never import outer ones.

## Layers
- `config.py` — `Settings` (pydantic-settings), one object for the whole service. Lives at the root of `app/`, not under `infra/` — it's a cross-cutting concern any layer's wiring may need, not owned by infra alone. Components take the values they need as constructor args (see `infra/db/session.py`, `deps.py`) instead of reading env vars themselves.
- `domain/` — plain Python (dataclasses, `Protocol`). No FastAPI/SQLAlchemy imports here.
- `services/` — business logic. Depends on `domain` Protocols, never on `infra` implementations directly.
- `infra/` — framework/DB specifics: SQLAlchemy models, session, concrete repository implementations of `domain` Protocols.
- `api/schemas/` — Pydantic request/response DTOs. Only imported inside `api/`, never by `domain`/`services` — that's why they live under `api/`, not as a sibling layer.
- `api/` — FastAPI routers. Wiring via `Depends` in `deps.py`. Converts schemas <-> domain objects.

## Adding a feature
One entity = one vertical slice, in this order: domain entity -> repository Protocol -> infra implementation -> service -> schema -> route. Don't create a layer that has nothing in it yet.

## Constraints
- No migrations: `infra/db/session.py` exposes `init_db()` (runs `Base.metadata.create_all`), called once from `main.py`'s `lifespan`. `main.py` calls `init_db()`, it never touches `Base`/`engine` directly — those are `infra`'s implementation detail. Add Alembic only if this outgrows an MVP.
- `DATABASE_URL` defaults to sqlite for local dev without docker; docker-compose overrides it to postgres.
- `main.py` is the composition root: it's the one place allowed to import from every layer to wire them together. That's not a layering violation — it just shouldn't reach past each layer's public entry point (e.g. `init_db()`, not `Base`/`engine`).

## Tests
- Functional style: plain functions, no test classes. One `client` fixture in `tests/conftest.py` (sets `DATABASE_URL` to a throwaway sqlite file before the app is imported, wipes it at session start), reused by every test file.
- Hit the actual HTTP routes through `client`, assert on status code + JSON body — don't unit-test service/repository internals in isolation, the route is the contract.
- To add a test: drop a new `tests/test_<thing>.py`, write `def test_...(client): ...`, copy the pattern from `tests/test_items.py`.

## Commands
- Package manager: `uv`. Run: `uv run uvicorn app.main:app --reload` (installs deps automatically).
- Lint + format: `uv run ruff format . && uv run ruff check .`. Config extends root `ruff.toml`.
- Tests: `uv run pytest`.

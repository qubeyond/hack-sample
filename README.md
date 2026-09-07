# sample

Шаблон репозитория для хакатона: бэкенд, фронтенд и ML-сервис — отдельные сервисы, связанные только через docker-compose и HTTP.

## Стек

- **backend** — FastAPI, Pydantic, SQLAlchemy, PostgreSQL, uv
- **frontend** — Vite, React, TypeScript, shadcn/ui, Tailwind v4, npm
- **ml** — FastAPI, uv

## Make

```
$ make help
запускать из корня репозитория

  make env            - скопировать .env.example -> .env везде, где его ещё нет

  make up             - весь стек в docker (сборка автоматически)
  make logs           - логи docker compose

  make backend-dev    - backend без docker (зависимости ставятся сами)
  make frontend-dev   - frontend без docker (зависимости ставятся сами)
  make ml-dev         - ml без docker (зависимости ставятся сами)

  make lint           - формат + линт всех сервисов
  make test           - тесты backend + ml
  make hooks          - поставить git pre-commit хуки (lint+format перед каждым коммитом)
```

## Пайплайн

1. Скопировать env-файлы: `make env`
2. Поставить git-хуки: `make hooks`
3. Работать в фиче-ветке от `main` (feat/fix/refactor)
4. Коммитить как обычно (Если очень нужно закоммитить черновик под дедлайн — `git commit --no-verify`)
5. Перед тем как считать задачу готовой — прогнать `make lint` и `make test` для своего сервиса
6. Открыть PR в `main` (CI гоняет lint + тесты только для push в `main` и для PR с целевой веткой `main`)
7. Заводить и закрывать задачи — в GitHub Projects

## Структура

```
sample/
├── .claude/skills/
├── .github/workflows/ci.yml
├── backend/
├── frontend/
├── ml/                      
├── docker-compose.yml       
└── Makefile                          
```

Каждый сервис (`backend/`, `frontend/`, `ml/`) — независимый: свои `.gitignore`, `.env.example` и `CLAUDE.md`.

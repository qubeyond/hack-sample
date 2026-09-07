# frontend

Vite + React + TS. Organized by feature, not by file type.

## Rules

- `features/<name>/{api.ts,types.ts,components/,hooks/}` — a feature owns everything it needs.
- `shared/` — only for code used by 2+ features (api client, ui primitives, generic helpers).
- A feature may import from `shared/`, never from another feature's internals.
- `app/` — shell only: routing, layout, providers. No business logic.
- API base URL comes from `VITE_API_URL`. Never hardcode the backend host.
- UI primitives come from shadcn/ui, styled with Tailwind. Add a new one with `npx shadcn@latest add <name>` — `components.json` is wired so it lands in `shared/ui/`, matching the folder convention above. Don't hand-roll a primitive shadcn already has.
- `cn()` in `shared/lib/utils.ts` merges Tailwind classes — use it instead of manual string concatenation for conditional classNames.
- The `@/` import alias points at `src/`. Existing app code uses relative imports; new shadcn-generated files use `@/...` — no need to migrate old files just to match.

## Commands

- Run: `npm install && npm run dev`.
- Lint + format: `npm run format && npm run lint`.

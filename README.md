# TaskFlow API
Developer handover for a junior DevOps training project. Read the three documents in `documents/` first.

Python 3.12; entry point `app.main:app`; HTTP port 8000.

For local development, use a Python virtual environment, install `requirements-dev.txt`, and run `python -m pytest -v` from the project root. Start the application with `python -m uvicorn app.main:app --host 0.0.0.0 --port 8000`.

Endpoints: `/` (homepage), `/health` (JSON health status), `/tasks` (sample read-only tasks), `/docs` (interactive API docs). No database or credentials required. APP_VERSION is optional; `.env.example` documents the variable, but the application does not automatically load .env files.

# Development team — application handover
Application: TaskFlow API. Runtime: Python 3.12. Framework: FastAPI. Server: Uvicorn. Entry point: app.main:app. Listen on 0.0.0.0:8000 inside the container.

Install runtime dependencies from requirements.txt; use requirements-dev.txt for testing. Run tests from the repository root using python -m pytest -v. All three tests must pass. Keep development dependencies out of the final runtime image where practical. Preserve the supplied application and tests during initial containerization.

Endpoints: GET / returns HTML; GET /health returns healthy status and version; GET /tasks returns two sample tasks; GET /docs provides API documentation. APP_VERSION is an optional environment variable. No database, secrets or persistent storage needed. This is a read-only demonstration service, not a full task management product.

DevOps owns Dockerfiles, ignore files, workflows, registry publishing and deployment configuration.

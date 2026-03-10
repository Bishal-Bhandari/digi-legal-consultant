from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)


@app.get("/")
async def root():
    return {"message": "AI Legal Analyzer API running"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}
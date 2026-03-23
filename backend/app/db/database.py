from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.mongo_url)
db = client["ai_legal_db"]


def get_database():
    return db
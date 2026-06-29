from __future__ import annotations

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from config.settings import settings

client: AsyncIOMotorClient | None = None
database: AsyncIOMotorDatabase | None = None


async def connect_to_mongo() -> None:
    global client, database

    if client is None:
        client = AsyncIOMotorClient(settings.mongodb_uri)
        database = client[settings.mongodb_db_name]


async def close_mongo_connection() -> None:
    global client, database

    if client is not None:
        client.close()
        client = None
        database = None


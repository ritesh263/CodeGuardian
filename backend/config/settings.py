from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mongodb_uri: str
    mongodb_db_name: str = "code_intelligence"
    jwt_secret_key: str
    access_token_expire_minutes: int = 720
    google_api_key: str = ""
    gemini_model: str = "gemini-3.5-flash"
    frontend_origin: str = "http://localhost:5173"


"""Runtime settings, read from environment variables (prefix JYOTISH_)."""

from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="JYOTISH_", env_file=".env", extra="ignore")

    env: Literal["local", "staging", "prod"] = "local"
    log_level: str = "INFO"
    max_followup_questions: int = 5
    session_ttl_hours: int = 24
    llm_provider: Literal["fake", "gemini", "claude"] = "fake"


@lru_cache
def get_settings() -> Settings:
    return Settings()

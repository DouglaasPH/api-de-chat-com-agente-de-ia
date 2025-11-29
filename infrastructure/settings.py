from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env")

    LLM_HOST: str
    LLM_PROVIDER: str
    LLM_MODEL: str
    LLM_TEMPERATURE: float = 0.0
    AGENT_NAME: str
    AGENT_INSTRUCTIONS: str


settings = Settings()

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LLM_HOST: str
    LLM_PROVIDER: str
    LLM_MODEL: str
    LLM_TEMPERATURE: float = 0.0
    
    AGENT_NAME: str 
    AGENT_INSTRUCTIONS: str
    
    class Config:
        env_file = ".env"


settings = Settings()

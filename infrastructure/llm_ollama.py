from strands.models import ollama
from infrastructure.settings import settings


def create_llm():
    """Cria o provider Ollama usando configurações do .env via settings."""
    return ollama.OllamaModel(
        model=settings.LLM_MODEL,
        temperature=settings.LLM_TEMPERATURE
    )

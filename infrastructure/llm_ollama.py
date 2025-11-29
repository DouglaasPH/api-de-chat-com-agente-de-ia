from strands.models import ollama
from infrastructure.settings import settings


def create_llm():
    """Cria o provider Ollama usando configurações do .env via settings."""
    return ollama.OllamaModel(
        host=settings.LLM_HOST,
        model_id=settings.LLM_MODEL,
        temperature=settings.LLM_TEMPERATURE,
    )

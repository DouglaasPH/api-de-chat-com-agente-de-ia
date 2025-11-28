from strands import Agent, RunConfig
from application.math_tool import calcular
from infrastructure.llm_ollama import create_llm
from infrastructure.settings import settings


class AgentService:
    def __init__(self):
        self.agent = Agent(
            name=settings.AGENT_NAME,
            instructions=settings.AGENT_INSTRUCTIONS,
            model=create_llm(),
            tools=[calcular],
        )
    
    def perguntar(self, prompt: str) -> str:
        result = self.agent.run(prompt, config=RunConfig(stream=False))
        return getattr(result, "output_text", None) or getattr(result, "message", str(result))
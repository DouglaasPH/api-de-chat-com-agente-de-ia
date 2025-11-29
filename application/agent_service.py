from strands.agent import Agent
from application.math_tool import calcular
from infrastructure.llm_ollama import create_llm
from infrastructure.settings import settings


class AgentService:
    def __init__(self):
        self.agent = Agent(
            name=settings.AGENT_NAME,
            description=settings.AGENT_INSTRUCTIONS,
            model=create_llm(),
            tools=[calcular],
        )
    
    async def perguntar(self, message: str) -> str:
        response = self.agent(message)
        message = response.message["content"][0]["text"]
        return message

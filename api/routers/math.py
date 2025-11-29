from fastapi import APIRouter

from application.agent_service import AgentService
from api.schemas.math_message import MathMessage


router = APIRouter()
agent_service = AgentService()


@router.post("/chat")
async def calcular_expressao(data: MathMessage):
    resposta = await agent_service.perguntar(data.message)
    return {"response": resposta}

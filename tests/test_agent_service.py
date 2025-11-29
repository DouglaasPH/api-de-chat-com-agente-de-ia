import pytest
from application.agent_service import AgentService

class MockAgent:
    def __call__(self, message):
        return type("Response", (), {"message": {"content": [{"text": f"eco: {message}"}]}})()

@pytest.fixture
def agent_service(monkeypatch):
    monkeypatch.setattr("application.agent_service.Agent", lambda **kwargs: MockAgent())
    from application.agent_service import AgentService
    return AgentService()

@pytest.mark.asyncio
async def test_perguntar(agent_service):
    resposta = await agent_service.perguntar("teste")
    assert resposta == "eco: teste"

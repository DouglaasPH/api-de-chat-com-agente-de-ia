from application.math_tool import calcular
from domain.math_service import MathService

def test_calcular_tool(monkeypatch):
    math_service = MathService()

    # Substitui MathService.calcular para garantir teste isolado
    monkeypatch.setattr(math_service, "calcular", lambda op, a, b: 42)

    result = calcular("soma", 1, 2)
    assert result == 3

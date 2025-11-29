from strands import tool
from domain.math_service import MathService


service = MathService()


@tool
def calcular(operacao: str, a: float, b: float):
    """
    Tool que expõe o domínio para o agente. Recebe strings simples
    (soma, subtracao, multiplicacao, divisao) ou sinais (+, -, *, /)
    """
    return service.calcular(operacao, a, b)

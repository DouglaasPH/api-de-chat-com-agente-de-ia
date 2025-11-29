import math


class MathService:
    """Lógica de domínio pura: apenas regras de negócio."""
    def calcular(self, operacao: str, a: float, b: float):
        if operacao in ("soma", "+"):
            return a + b
        if operacao in ("subtracao", "-"):
            return a - b
        if operacao in ("multiplicacao", "*"):
            return a * b
        if operacao in ("divisao", "/"):
            if b == 0 :
                return "Erro: divisão por zero."
            return a / b
        if operacao in ("potencia", "**", "pow"):
            return a ** b
        if operacao in ("raiz", "sqrt"):
            if a < 0:
                return "Erro: raiz de número negativo."
            return math.sqrt(a)
        return "Operação inválida. Use soma, subtração, multiplicação ou divisão."

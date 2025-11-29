import math
import pytest

from domain.math_service import MathService


@pytest.fixture
def service():
    return MathService()


def test_soma(service):
    assert service.calcular("soma", 3, 2) == 5
    assert service.calcular("+", 1.5, 2.5) == 4.0


def test_subtracao(service):
    assert service.calcular("subtracao", 5, 3) == 2
    assert service.calcular("-", 10, 4) == 6


def test_multiplicacao(service):
    assert service.calcular("multiplicacao", 3, 4) == 12
    assert service.calcular("*", 2.5, 2) == 5.0


def test_divisao(service):
    assert service.calcular("divisao", 8, 2) == 4
    assert service.calcular("/", 9, 3) == 3


def test_divisao_por_zero(service):
    assert service.calcular("divisao", 5, 0) == "Erro: divisão por zero."


def test_potencia(service):
    assert service.calcular("potencia", 2, 3) == 8
    assert service.calcular("pow", 3, 2) == 9
    assert service.calcular("**", 5, 2) == 25


def test_raiz_quadrada(service):
    assert service.calcular("raiz", 9, None) == 3
    assert service.calcular("sqrt", 16, None) == 4


def test_raiz_numero_negativo(service):
    assert service.calcular("raiz", -9, None) == "Erro: raiz de número negativo."


def test_operacao_invalida(service):
    assert "Operação inválida" in service.calcular("qualquer", 1, 2)
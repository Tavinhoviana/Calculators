from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4, BrokenHandler

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandlerError:
    def average(self, numbers: List[float]) -> float:
        return 3
    
class MockCorrectHandler:
    def average(self, numbers: List[float]) -> float:
        return sum(numbers) / len(numbers)

# Teste de sucesso
def test_calculate_success():
    num = [2, 4, 8, 8]
    mock_request = MockRequest({"numbers": num})
    calculator = Calculator4(MockCorrectHandler())

    response = calculator.calculate(mock_request)

    # Calcula a média automaticamente
    average_final = sum(num) / len(num)

    assert response["data"]["value"] == average_final
    assert response["data"]["sucess"] is True
    print(f"Média calculada: {response['data']['value']}")

# Teste de exceção (média inconsistente)
def test_calculate_with_exception():
    mock_request = MockRequest({"numbers": [10, 20, 30, 70]})
    calculator = Calculator4(BrokenHandler())

    with raises(Exception) as exinfo:
        calculator.calculate(mock_request)

    assert str(exinfo.value) == "Falha no processo: Média inconsistente com a soma"
    print(exinfo.value)
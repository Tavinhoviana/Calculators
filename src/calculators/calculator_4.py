from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpUBadRequestError

class BrokenHandler:
    def average(self, numbers):
        return 999  # valor errado proposital

class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler
    
    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        total_sum = self.__calculate_sum(input_data)
        average = self.__calculate_average(input_data)
        
        self.__verify_result(average, total_sum, len(input_data))

        formated_response = self.__format_response(average)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")
    
        input_data = body["numbers"]
        return input_data
    
    def __calculate_sum(self, numbers: List[float]) -> float:
        total = 0
        for num in numbers: total += num
        return total
    
    def __calculate_average(self, numbers: List[float]) -> float:
        average = self.__driver_handler.average(numbers)
        return average

    def __verify_result(self, average: float, total_sum: float, count: int) -> None:
        if not abs((average * count) - total_sum) < 1e-9:
            raise HttpUBadRequestError("Falha no processo: Média inconsistente com a soma")
        
    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "value": float(average),
                "sucess": True
            }
        }



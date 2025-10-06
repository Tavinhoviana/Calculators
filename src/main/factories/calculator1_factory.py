from src.calculators.calculator_1 import Calculator1
from src.drivers.numpy_handler import NumpyHandler

def calculator1_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator1 (numpy_handler)
    return calc
import Pyro4
from Calculator import Calculator

@Pyro4.expose
class CalculatorImpl(Calculator):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise Exception("Cannot divide by zero")
        return a / b
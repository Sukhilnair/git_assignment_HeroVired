import math

class Calculator:
    def add(self, operand1, operand2):
        """Adds two numbers."""
        return operand1 + operand2

    def subtract(self, operand1, operand2):
        """Subtracts the second number from the first."""
        return operand1 - operand2

    def multiply(self, operand1, operand2):
        """Multiplies two numbers."""
        return operand1 * operand2

    def divide(self, dividend, divisor):
        """
        Divides the first number by the second.
        Raises a ValueError if the divisor is zero.
        """
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        return dividend / divisor

    def square_root(self, x):
        """Calculates the square root of a number."""
        return math.sqrt(x)

if __name__ == "__main__":
    # Example usage
    calculator = Calculator()
    num1 = 16
    num2 = 0

    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

    num3 = 25
    print(f"The square root of {num3} = {calculator.square_root(num3)}")

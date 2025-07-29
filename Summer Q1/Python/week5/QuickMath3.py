# 1. Create a class called calculator
class Calculator:
    
    # 2. Function for addition
    def add(self, a, b):
        return a + b

    # Function for subtraction
    def subtract(self, a, b):
        return a - b

    # Function for multiplication
    def multiply(self, a, b):
        return a * b

    # Function for division
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

# 3. Create an instance of your calculator class
calc = Calculator()

# 4. Call each function and store the result in a variable
add_result = calc.add(10, 5)
subtract_result = calc.subtract(10, 5)
multiply_result = calc.multiply(10, 5)
divide_result = calc.divide(10, 5)

# 5. Print all your variables to the console
print("Addition:", add_result)
print("Subtraction:", subtract_result)
print("Multiplication:", multiply_result)
print("Division:", divide_result)

class Calculator:
    def __init__(self):
        self.result = 0
        pass
    def add(self, n):
        self.result += n
    
    def subtract(self, n):
        self.result -= n
    
    def multiply(self, n):
        self.result *= n
    
    def devide(self, n):
        self.result /= n

    def clear(self):
        self.result = 0
    
    def get_result(self):
        return self.result

calc = Calculator()
calc.add(10)
calc.multiply(2)
calc.subtract(5)
print(calc.get_result())
calc.devide(3)
print(calc.get_result())

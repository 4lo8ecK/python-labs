class Temperature:
    def __init__(self, t) -> None:
        self.t = t
    
    def to_fahrenheit(self):
        return self.t * 9/5 + 32
    def to_kelvin(self):
        return self.t + 273.15
    def is_freezing(self):
        return self.t < 0

t = Temperature(-5)
print(t.to_fahrenheit()) # 23
print(t.is_freezing()) # true
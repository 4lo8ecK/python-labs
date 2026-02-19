class Student:
    def __init__(self, fio: str, age: int, _grade: list[int]):
        self.name = fio
        self.age = age
        self.grade = []
        for i in _grade:
            if self._in_rng(i):
                self.grade += [i]
    
    @staticmethod
    def _in_rng(n: int) -> bool:
        return 2 <= n <= 5
    
    def average_grade(self) -> float:
        return round(sum(self.grade)/len(self.grade), 2)
    
    def has_excellent_grades(self) -> bool:
        return 5 in self.grade

s = Student("Иванов И.И.", 20, [4, 5, 4, 5])
print(s.average_grade()) # 4.5
print(s.has_excellent_grades()) # true
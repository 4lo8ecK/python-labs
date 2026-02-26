class Student:
    def __init__(self, name: str, age: int, grade: int) -> None:
        self.name = name
        self.age = age
        if self._grade_in_range(grade):
            self.grade = grade

    def __str__(self) -> str:
        return f"Имя: {self.name}, возраст: {self.age}\nОценка - {self.grade} ({self.is_passed()})"

    @staticmethod
    def _grade_in_range(grade: int) -> bool:
        if 1 <= grade <= 5:
            return True
        raise ValueError("'grade: int' должен быть от 1 до 5")

    def is_passed(self, grade: int|None = None) -> str:
        _grade = -1
        if grade == None:
            _grade = self.grade
        else:
            _grade = grade
        if _grade >= 3:
            return "Сдал"
        return "Не сдал"

gleb = Student("Глеб", 18, 5)
print(gleb)
print(gleb.is_passed())
print(gleb.is_passed(3))
print(gleb.is_passed(2))

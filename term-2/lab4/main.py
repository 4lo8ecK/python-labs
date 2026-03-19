DBG = True

class Timer:
    def __init__(self, h: int = 0, m: int = 0, s: int = 0) -> None:
        if not(0 <= s < 60 or 0 <= m < 60):
            raise ValueError("Секунды или минуты должны быть в промежутке от 0 до 59")
        if not(0<= h <= 24):
            raise ValueError("Часы должны быть в промежутке от 0 до 24")

        self.hours = h
        self.mins = m
        self.sec = s
    
    def __del__(self) -> None:
        del self.hours
        del self.mins
        del self.sec

        if DBG: print("вызван деструктор класса Timer")
    
    def __str__(self) -> str:
        return f"Timer: часы: {self.hours}, минуты: {self.mins}, секунды: {self.sec}"
    
    def add_100_min(self) -> None:
        summ = self.mins + 100
        hours_to_add = summ // 60
        delta = summ - (60 * hours_to_add)
        self.hours += hours_to_add
        self.mins = delta

    def minutes_to_midnight(self) -> int:
        mins_in_day = 24 * 60
        mins = self.hours * 60 + self.mins
        return mins_in_day - mins

class Timetable(Timer):
    def __init__(self) -> None:

        pass

    def __str__(self) -> str:

        pass

    pass

if __name__ == "__main__":
    a = Timer()
    a.add_100_min()
    print(a)
    print(a.minutes_to_midnight())
import colors as col

DBG = True

# константы
CLS = '\x1bc'

SUBJ    = 'subj'
TIME    = 'time'
AUD     = 'aud'

class Time:
    def __init__(self, h: int = 0, m: int = 0, s: int = 0) -> None:
        if not(0 <= s < 60 or 0 <= m < 60):
            raise ValueError("Секунды или минуты должны быть в промежутке от 0 до 59")
        if not(0<= h <= 24):
            raise ValueError("Часы должны быть в промежутке от 0 до 24")

        self.hours = h
        self.minutes = m
        self.seconds = s
        
        if DBG: print(col.style(col.dim, col.yellow), "вызван конструктор класса Time", col.style(0), sep='')

    
    def __del__(self) -> None:
        del self.hours
        del self.minutes
        del self.seconds
        if DBG: print(col.style(col.dim, col.yellow), "вызван деструктор класса Time", col.style(0), sep='')
    
    def __str__(self) -> str:
        return f"Time({self.hours}:{self.minutes}:{self.seconds})"
    
    # "приватные" методы
    def __add_n_min(self, n: int = 0) -> None:
        summ = self.minutes + n
        hours_to_add = summ // 60
        delta = summ - (60 * hours_to_add)
        self.hours += hours_to_add
        self.minutes = delta

    @staticmethod
    def _get_time_added_n(time: Time = None, n: int = 0) -> Time:
        if Time == None or not isinstance(time, Time):
            raise ValueError("аргумент time должен иметь значение")
        mins_summ = time.minutes + n
        hours_to_add = mins_summ // 60
        delta = mins_summ - (60 * hours_to_add)
        return Time(time.hours + hours_to_add, delta, time.seconds)

    # методы задания
    def add_100_min(self) -> None:
        self.__add_n_min(100)

    def minutes_to_midnight(self) -> int:
        mins_in_day = 24 * 60
        minutes = self.hours * 60 + self.minutes
        return mins_in_day - minutes

class Timetable(Time):
    LESSON_LEN = 80 # min

    def __init__(self, h: int = 0, m: int = 0, s: int = 0, lessons: list[dict] = None) -> None:
        super().__init__(h, m, s)
        if lessons == None or not isinstance(lessons, list):
            raise ValueError("некорректные данные переданы как расписание")
        for i in lessons:
            keys_lst = i.keys()
            if not(SUBJ in keys_lst) or not(TIME in keys_lst) or not(AUD in keys_lst):
                lessons.remove(i)
                if DBG: print(col.style(col.dim, col.red), 'DELETE: ', col.style(col.dim), i, col.style(col.dim, col.italic, col.yellow), ' has been removed', col.style(0), sep='')
        if DBG: print(col.style(col.dim), 'Итоговый список:\n', lessons, col.style(0), sep='')
        self.lessons = lessons
        if DBG: print(col.style(col.dim, col.yellow), "вызван конструктор класса Timetable", col.style(0), sep='')


    def subject_start(self) -> str:
        for i in self.lessons:
            # l_t <- Lesson_Time
            # le_t <- LessonEnd_Time
            l_t = i[TIME] 
            le_t = Time._get_time_added_n(i[TIME], self.LESSON_LEN) 
            if ((l_t.hours <= self.hours <= le_t.hours) and
                (l_t.minutes <= self.minutes <= le_t.minutes) and
                (l_t.seconds <= self.seconds <= le_t.seconds)):
                return i[SUBJ]
        return "Занятий нет"

    def __str__(self) -> str:
        return f"Timetable: time({self.hours}, {self.minutes}, {self.seconds}), subject: {self.subject_start()}"
        pass
    
    def __del__(self) -> None:
        super().__del__()
        del self.lessons
        if DBG: print(col.style(col.dim, col.yellow), "вызван деструктор класса Timetable", col.style(0), sep='')
    pass

if __name__ == "__main__":

    print(CLS)
    cmd = input('Показывать отладочную информацию? (y/N): ')
    if cmd == 'y' or cmd == 'Y' or cmd == 'Н' or cmd == 'н':
        DBG = True
    else:
        DBG = False
    print(CLS)

    lessons_list = [
        {SUBJ: 'Линейная алгебра',                    TIME: Time(8, 20),    AUD: '2-06'},
        {SUBJ: 'Программирование в Python',           TIME: Time(9, 50),    AUD: 'I-321'},
        {SUBJ: 'Программирование в Python',           TIME: Time(9, 50),    'auditory': 'I-321'},
        {SUBJ: 'Иностранный язык',                    TIME: Time(11, 40),   AUD: 'I-314'},
        {SUBJ: 'Введение в искусственный интеллект',  TIME: Time(13, 30),   AUD: 'I-306'}]

    print('\n\t', col.style(1, 21, 33), '=== Проверки для Time ===', col.style(0), '\n')
    
    print(col.style(1), 'Проверка 1:', col.style(0), sep='')
    a = Time()
    print(col.style(32), 'Инициализация Time без аргументов:\t',col.style(), a, sep='')
    a.add_100_min()
    print(col.style(32), 'Добавление 100 минут:\t\t\t',col.style(), a, sep='')
    print(col.style(32), 'Количество минут до полуночи:\t\t',col.style(), a.minutes_to_midnight(), sep='')

    print()

    print(col.style(1), 'Проверка 2:', col.style(0), sep='')
    b = Time(15, 8, 68)
    print(col.style(32), 'Инициализация Time с (15, 8, 68):\t',col.style(), b, sep='')
    b.add_100_min()
    print(col.style(32), 'Добавление 100 минут:\t\t\t',col.style(), b, sep='')
    print(col.style(32), 'Количество минут до полуночи:\t\t',col.style(), b.minutes_to_midnight(), sep='')
    
    print()
    del a
    del b

    print('\n\t', col.style(1, 21, 33), '=== Проверки для Timetable ===', col.style(0), '\n')
    print(col.style(1), 'Проверка 1:', col.style(0), sep='')

    a = Timetable(lessons=lessons_list)
    print(col.style(32), 'Инициализация Timetable без аргументов:\t', col.style(), a, sep='')
    print(col.style(32), 'Дисциплина, в указанное время:\t\t', col.style(), a.subject_start(), sep='')

    print()

    print(col.style(1), 'Проверка 2:', col.style(0), sep='')

    b = Timetable(8, 30, 0, lessons_list)
    print(col.style(32), 'Инициализация Timetable (8, 30, 0):\t', col.style(), b, sep='')
    print(col.style(32), 'Дисциплина, в указанное время:\t\t', col.style(), b.subject_start(), sep='')

    print()
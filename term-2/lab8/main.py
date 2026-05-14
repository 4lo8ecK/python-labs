# region impports
import random as rnd
import sqlite3
# endregion

# region constants
DBG = False
CLS = '\x1bc'
NAMES_BANK = ['Глеб', 'Рома', 'Дима', 'Илья']
SNAMES_BANK = ['Иванов', 'Петров', 'Васильев', 'Кузнецов',]
VACANCIES = ['Игрок в Brawl Stars', 'Программист на Brainfuck', 'Программист на C++', 'Программист на Python', '3D аниматор в Autodesk Maya', '3D моделлер в Autodesk 3DsMax']
CANDIDATES_COUNT = 24
#endregion 

# region helper functions
def get_rnd(lst: list):
    return lst[rnd.randint(0, len(lst)-1)]
#endregion

# region Lab8 class definition
class Lab8:
    def __init__(self):
        if DBG: print("\x1b[0;1;31m=== CALLED CLASS INIT ===\x1b[0m")

        self.mydb = sqlite3.connect('lab8.db')
        self.cur = self.mydb.cursor()
        self.init_database()

    def __del__(self):
        if DBG: print("\x1b[0;1;31m=== CALLED DESTRUCTOR ===\x1b[0m")
        self.mydb.commit()
        self.mydb.close()

    def table_is_empty(self, table_name: str) -> bool:
        self.cur.execute(f"SELECT EXISTS (SELECT 1 FROM {table_name})")
        return self.cur.fetchone()[0] == 0

    def init_database(self):
        # создание таблицы с кандидатами
        self.cur.execute("CREATE TABLE IF NOT EXISTS candidates ( id INTEGER, name TEXT, surname TEXT);")
        
        # проверка на существование для заполнения
        if self.table_is_empty("candidates"):
            candidates = []
            for i in range(CANDIDATES_COUNT):
                candidates += [(int(i), str(get_rnd(NAMES_BANK)), str(get_rnd(SNAMES_BANK)))]
            self.cur.executemany("INSERT INTO candidates (id, name, surname) VALUES (?, ?, ?)", candidates)

        # создание таблицы с вакансиями
        self.cur.execute("CREATE TABLE IF NOT EXISTS vacancy ( id INTEGER, name TEXT);")
        if self.table_is_empty("vacancy"):
            vacancy_lst = []
            for i in range(len(VACANCIES)):
                vacancy_lst += [(int(i), VACANCIES[i])]
            self.cur.executemany("INSERT INTO vacancy (id, name) VALUES (?, ?)", vacancy_lst)

        # создание таблицы с заявками 
        self.cur.execute("CREATE TABLE IF NOT EXISTS applications ( id INTEGER, candidate_id INTEGER, vacancy_id INTEGER)")
        if self.table_is_empty("applications"):
            APPS_COUNT = 54
            apps_lst = []
            for i in range(APPS_COUNT):
                apps_lst += [(int(i), rnd.randint(0, CANDIDATES_COUNT-1), rnd.randint(0, len(VACANCIES)-1))]
            self.cur.executemany("INSERT INTO applications (id, candidate_id, vacancy_id) VALUES (?, ?, ?)", apps_lst)

    def task1(self) -> None:
        self.cur.execute('''SELECT candidates.name, candidates.surname, vacancy.name as vacancy
        FROM candidates
        JOIN applications ON candidates.id = applications.candidate_id  
        JOIN vacancy ON applications.vacancy_id = vacancy.id;''')
        for row in self.cur.fetchall():
            print(f"\x1b[0;1;33m{row[0]} {row[1]}:\t\x1b[0;32m{row[2]}\x1b[0m")

    def task2(self, id: int = 1) -> None:
        self.cur.execute(f"SELECT name, surname FROM candidates WHERE id = {id}")
        candidate = self.cur.fetchone()

        if candidate is None:
            raise ValueError("Нет кандидата с таким id")

        self.cur.execute(f"""SELECT vacancy.name AS vacancy FROM vacancy
        JOIN applications ON vacancy.id = applications.vacancy_id
        WHERE applications.candidate_id = {id};""")

        count = 1
        print(f"\x1b[0;1;33m{candidate[0]} {candidate[1]}\x1b[0m:")
        for row in self.cur.fetchall():
            print(f"\x1b[0;33m{count}\x1b[0m) \x1b[0;32m{row[0]}\x1b[0m")
            count += 1

    def task3(self) -> None:
        self.cur.execute("""SELECT vacancy.name as vacancy, COUNT(applications.id) as apps_count
        FROM vacancy LEFT JOIN applications ON vacancy.id = applications.vacancy_id
        GROUP BY vacancy.id;""")
        for row in self.cur.fetchall():
            print(f"\x1b[0;32m{row[0]}\x1b[0m: \x1b[0;33m{row[1]}\x1b[0")
#endregion

# region int main() // :P
if __name__ == "__main__":
    print(CLS, "\n\t\x1b[0;1;33;21m== Лабораторная работа №8 ==\x1b[0m\n")
    app = Lab8()
    print("\n\tЗадание 1\n")
    app.task1()
    print("\n\tЗадание 2\n")
    app.task2(1)
    print("\n\tЗадание 3\n")
    app.task3()

# endregion
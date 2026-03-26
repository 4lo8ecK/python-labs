import os
from student import Student
import colors as col

DBG = True
CSV_SEP = ';'

class App:
    
    APP_FILES_DIR = 'files'
    FILENAME = 'students.csv'
    
    def __init__(self) -> None:
        if not os.path.isdir(self.APP_FILES_DIR):
            os.mkdir(self.APP_FILES_DIR)
            if DBG: print(f'Создана директория "{self.APP_FILES_DIR}"')

        pt = os.path.join(self.APP_FILES_DIR, self.FILENAME)
        if not os.path.exists(pt):
            self.__file_handle = open(pt, 'w', encoding='utf-8')
            self.gen_file_data()

        self.__file_handle = open(pt, 'r', encoding='utf-8')

        if DBG: print('Вызван конструктор класса \'App\'')

    def __del__(self) -> None:
        self.__file_handle.close()

        if DBG: print('Вызван деструктор класса \'App\'')

    @staticmethod
    def tuple_to_csv_line(tpl: tuple) -> str:
        return CSV_SEP.join(str(i) for i in tpl)

    def writeln(self, line: str = None) -> bool:
        if line != None and isinstance(line, str):
            self.__file_handle.write(f'{line}\n')

    def gen_file_data(self, lines_count = 500000) -> None:
        to_csv = App.tuple_to_csv_line
        for i in range(lines_count):
            self.writeln(to_csv(Student.get_random().to_tuple()))
        if DBG: print('Сгенерированы случайные данные')

    def get_file_handler(self):
        return self.__file_handle

if __name__ == '__main__':
    cmd = input('Показывать отладочную информацию? (y/N): ')
    if cmd == 'y' or cmd == 'Y' or cmd == 'Н' or cmd == 'н':
        DBG = True
    else:
        DBG = False

    app = App()

    town = 'Москва'
    mariage = 'состоит в браке'
    
    stud_list = []

    for i in app.get_file_handler():
        lst = i.split(CSV_SEP)
        lst[4] = lst[4].strip()
        if lst[3] == town and lst[4] == mariage:
            stud_list += [Student(*tuple(lst))]
    
    found_students = open(os.path.join(App.APP_FILES_DIR, 'found.csv'), 'w', encoding='utf-8')

    for i in stud_list:
        # if DBG: print(i)
        found_students.write(str(i) + '\n')
    if DBG: print('Полученные результаты записаны в файл \'files/found.csv\'')

    found_students.close()
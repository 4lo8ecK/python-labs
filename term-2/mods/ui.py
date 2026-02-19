# python module myui for python labs in university
import colors as col
import sys
# import os

CLEAR_CONSOLE = '\x1bc'
CMD_ARROW = col.style(col.bold, col.cyan) + '→' + col.style(0)

EXIT_CODES = ['exit', 'quit', 'q', 'учше', 'йгше', 'й', 'выход']

def cls() -> None:
    print(CLEAR_CONSOLE, end='')
# !cls()


class ui:
    def __init__(self, lab_number: int = -1, descr: str = '', tasks: list = []) -> None:
        self._lab: int = lab_number
        self._description: str = descr
        self._tasks: list = tasks

    # end of '__init__(self, int, str, list) -> None'
    
    # def _cmd_proc(self, command: str = '') -> None:
    #     if command in EXIT_CODES:
    #         sys.exit()
    # # end of 'cmd_proc(self, str) -> None'
    
    def _cmd(self) -> str:
        cmd = ''
        try:
            cmd = input(CMD_ARROW + ' ')
            if cmd in EXIT_CODES:
                sys.exit(0)
        except SystemExit and KeyboardInterrupt:
            cls()
            sys.exit(0)
        return cmd

    def _show_header(self) -> None:
        lab_num = ''
        # Всё это для красивого заголовка "Лабораторная работа №N"
        if self._lab != -1:
            lab_num: str = "\n\t" + col.style(col.bold) +\
                    "Лабораторная работа " + \
                    col.style(col.bold, col.yellow, col.italic) +\
                    str(self._lab) + col.style(0)
        #endif
        
        # Описание (подзаголовок)
        lab_descr = ''
        if self._description != '':
            lab_descr: str = "\t" + col.style(col.dim, col.italic) + \
                    self._description + col.style(0)
        #endif

        print(lab_num)
        print(lab_descr)
        print("")
    #end of '_show_header(self) -> None'

    def _exec_task(self, number: int) -> None:
        tasks_count: int = len(self._tasks)
        if not (0 < number <= tasks_count): return
        cls()
        self._show_header()
        self._tasks[number - 1]()
        print('')
        self._cmd()
        print('')
    # end of '_exec_task(self, int) -> None'

    def _exec_iteration(self) -> None:
        self._show_header()

        tasks_count: int = len(self._tasks)
        print("%sКоличество заданий: %s%d%s\n" % \
                (col.style(col.italic),\
                col.style(col.bold, col.italic, col.yellow),\
                tasks_count,\
                col.style(0)))

        cmd: str = self._cmd()
        try:
            self._exec_task(int(cmd))
        except ValueError:
            return
        #end try
    # end of '_exec_iteration(self) -> None' 
    
    def exec(self) -> None:
        while True:
            cls()
            self._exec_iteration()
        #endloop
    # end of 'exec(self) -> None'

# endclass
def tsk1() -> None:
    print("Hello, World")

def tsk2() -> None:
    cmd: str = input("Введите значение: ")
    print(f"Введёное вами значение: {cmd}")

tsks = [tsk1, tsk2]

app: ui = ui(12, "Просто подзаголовок", tsks)
app.exec()

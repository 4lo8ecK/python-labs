# Лабораторная работа №15
# Вариант 6
# Гаврилов Павел ФМ-11-25

import os
import myui

COMMANDS_STR = ['DEPOSIT', 'WITHDRAW', 'BALANCE', 'TRANSFER', 'INCOME']
ERR_MSG = 'ERROR'

DIR_NAME = 'lab15-files'
DATA_BASE_FILE = 'comands'

LAB_HEAD = '\x1bc\n\t\x1b[1m\x1b[3m\x1b[21mЛабораторная работа №15\x1b[0m\n'

g_clients = {}

LAB_HEAD = '\x1bc\n\t\x1b[1m\x1b[3m\x1b[21mЛабораторная работа №15\x1b[0m\n'

#region MAIN METHODS
def deposit(client: str, balance: int = 0) -> bool:
    try:
        balance = int(balance)
        g_clients.update({client: balance})
        return True
    except:
        return False
# !add_client(str, int) -> bool

def withdraw(client: str, summ: int = 0) -> bool:
    try:
        summ = int(summ)
        balance = g_clients.get(client)
        balance -= summ
        g_clients.update({client: balance})
        return True
    except:
        return False
# !withdraw(str, int) -> bool

def balance(client: str) -> int:
    try:
        return g_clients.get(client)
    except:
        return None
# !balance(str) -> int

def transfer(name1: str, name2: str, summ: int) -> bool:
    try:
        summ = int(summ)
        clients_list = list(g_clients.keys())
        if name1 not in clients_list:
            deposit(name1)
        if name2 not in clients_list:
            deposit(name2)
    
        n1_balance = balance(name1) - summ
        n2_balance = balance(name2) + summ
    
        deposit(name1, n1_balance)
        deposit(name2, n2_balance)

        return True
    except:
        return False
# !transfer(str, str, int) -> bool

def income(proc: int) -> bool:
    try:
        proc = int(proc)
        clients = list(g_clients.keys())
        for c in clients:
            bal = balance(c)
            bal = int(bal * (1 + proc/100))
            g_clients.update({c: bal})
        return True
    except:
        return False
# !income(int) -> bool

# порядок функций ДОЛЖЕН быть идентичным в FUNCTIONS_LIST и COMMANDS_STR
FUNCTIONS_LIST = [deposit, withdraw, balance, transfer, income]

#endregion
#region INIT
def read_file() -> list:
    cmdlines = []
    with open(file=os.path.join(DIR_NAME, DATA_BASE_FILE), mode='r', encoding='utf-8') as file:
        cmdlines = file.readlines()
    return cmdlines

def init_prog(commands: list = []) -> None:
    if not os.path.exists(DIR_NAME):
        os.mkdir(DIR_NAME)
    for i in range(len(commands)):
        commands[i] += '\n'
    with open(file=os.path.join(DIR_NAME, DATA_BASE_FILE), mode='w', encoding='utf-8') as file:
        file.writelines(commands)
#endregion
#region PARCER
def parce_line(line: str) -> bool:
    # print(line)
    line: list = line.split()
    func_index: int = -1
    try:
        func_index: int = COMMANDS_STR.index(line[0])
    except ValueError:
        return
    args = line[1:len(line)]
    return FUNCTIONS_LIST[func_index](*args)
#endregion
#region UI
commands_from_task = [
    'DEPOSIT Ivanov 100',
    'INCOME 5',
    'BALANCE Ivanov',
    'TRANSFER Ivanov Petrov 50',
    'WITHDRAW Petrov 100',
    'BALANCE Petrov',
    'BALANCE Sidorov'
]

def run_task() -> None:
    print(LAB_HEAD)
    print('\x1b[3m\x1b[4mВывод:\x1b[0m')

    with open(file=os.path.join(DIR_NAME, DATA_BASE_FILE), mode='r', encoding='utf-8') as file:
        balance_counter = 1
        while True:
            cmd = file.readline()
            if not cmd:
                break
            res = parce_line(cmd)
            if not isinstance(res, bool):
                txt_to_write = ''
                if res == None:
                    txt_to_write = ERR_MSG 
                elif isinstance(res, int):
                    txt_to_write = str(res)
                space = ' ' * (3 - len(str(balance_counter)))
                print(f'\x1b[100m{space}{balance_counter}|\x1b[0m {txt_to_write}')
                balance_counter += 1
    print('')
    g_clients.clear()

def show_commands() -> None:
    print(LAB_HEAD)
    print('\x1b[3m\x1b[4mКоманды в файле:\x1b[0m')
    
    commands = read_file()
    length = len(commands)
    for i in range(length):
        space = ' ' * (len(str(length)) - len(str(i)))
        print(f'\x1b[100m{space}{i}|\x1b[0m {commands[i]}', end='')
    print('')

ui_txt = [
    LAB_HEAD,
    'Выберите опцию:',
    '\t[1] - вывод результата',
    '\t[2] - показать спиок команд'
]
funcs_list = [run_task, show_commands]

init_prog(commands_from_task)
myui.exec(funcs_list, ui_txt)
#endregion

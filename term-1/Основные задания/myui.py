# Это попытка автоматизировать процесс создания UI в лабораторных работах

import sys

EXIT_CODES = ['exit', 'quit', 'q', 'выход', 'учше', 'йгше', 'й'] 

def _load_codes(path: str) -> list:
    codes = []
    try:
        with open(path, 'r') as file:
            codes = file.readlines()
            for i in range(len(codes)):
                codes[i] = codes[i][:-1]
    except FileNotFoundError:
        return codes
    return codes

def clear_console() -> None:
    print('\033c', end='')

def main(funcs: list, txt: list = []) -> None:
    
    # Вывод в консоль данных
    for i in txt:
        print(i)
    
    cmd = input('→ ')
    if cmd in EXIT_CODES: sys.exit(0)

    try:
        cmd = int(cmd)
    except ValueError:
        return

    while True:
        clear_console()
        if 1 <= cmd <= len(funcs):
            funcs[int(cmd) - 1]()           
        lcmd = input('→ ')
        if lcmd == '': continue
        if lcmd in EXIT_CODES: return 

def exec(funcs: list, txt: list = []) -> None:
    while True:
        clear_console()
        main(funcs, txt)

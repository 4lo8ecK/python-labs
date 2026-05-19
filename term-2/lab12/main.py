import re

# region task 1

def no_literals(text: str) -> bool:
    pattern = r"[a-zA-Zа-яА-ЯёЁ]"
    return not re.search(pattern, text)

# endregion
# region task 2

def a_to_argh(text: str) -> None:
    pattern = r"\b[aAаА]+\b"
    lines = text.split('\n')
    with open('text_new.txt', mode='a', encoding='utf-8') as fl:    
        for line in lines:
            new_line = re.sub(pattern, 'argh', line, count=1)
            fl.write(new_line)

#endregion
# region task 3

def del_symbols(text: str) -> None:
    pattern = r"[^\w@.-]"
    res = re.sub(pattern, '', text)
    with open('text_new_2.txt', mode='w', encoding='utf-8') as fl:
        fl.write(res)

#endregion

if __name__ == "__main__":
    print(no_literals('hello'))
    with open('text.txt', mode='r', encoding='utf-8') as fl:
        all_text = fl.read()
        a_to_argh(all_text)
        del_symbols(all_text)

    
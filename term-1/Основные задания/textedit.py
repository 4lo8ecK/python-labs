# textedit - модуль для упрощения рутинной работы с текстом

# Удаляет лишние пробелы из текста
def normalize(text: str, separator: str = '') -> str:
    return separator.join(text.split())

# Возвращает строку, 
def normalize(lst: list, separator: str = '') -> str:
    return separator.join(lst)

# Создаёт список из строк, разделённых с помощью '\n'
def getlines(text: str) -> list:
    return text.split('\n')
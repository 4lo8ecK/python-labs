class Task:

    st_new = 1
    st_in_prog = 2
    st_done = 3

    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description
        self.status = self.st_new

    def __str__(self) -> str:
        return f"Задача: {self.title}\nДоп.: {self.description}\n---\nСтатус: {self.str_status(self.status)}"

    @staticmethod
    def str_status(self, status: int) -> str:
        if status == self.st_new: return "новая"
        elif status == self.st_in_prog: return "в процессе"
        elif status == self.st_done: return "выполнена"

    def mark_in_progress(self) -> None:
        self.status = self.st_in_prog

    def mark_done(self) -> None:
        self.status = self.st_done

    def update_description(self, descr: str|None = None) -> None:
        if descr != None: self.description = descr

    def is_done(self) -> bool:
        return self.status == self.is_done


task = Task("Сделать домашку", "Написать программу на Python")
task.mark_in_progress()
print(task.is_done)
import tkinter as tk
from tkinter import messagebox

SEGOE_UI = ("Segoe UI", 24)
TIMES_NEW_ROMAN = ("Times New Roman", 24)

DBG = False
def stdlog(*args,**kwargs):
    try:
        if DBG:
            print('\x1b[33m', *args, '\x1b[0m', **kwargs)
    except: pass
def errlog(*args,**kwargs):
    try:
        if DBG:
            print('\x1b[31;1m', *args, '\x1b[0m', **kwargs)
    except: pass

class Lab10:
    def __init__(self) -> None:
        self.font_id = 0

        stdlog('Инициализация экземпляра класса Lab10')
        self.rt = tk.Tk()
        self.__init_tk_root()
        self.__init_menu()
        self.__init_context_menu()
        
        self.main_lbl = tk.Label(self.rt, text='Фамилия', font=SEGOE_UI)
        self.show_label()
        
        self.rt.mainloop()

    def __del__(self) -> None:
        stdlog('Вызван деструктор класса Lab10')
        self.quit()

    def __init_tk_root(self) -> None:
        stdlog('Инициализация tkinter.root')
        root = self.rt
        root.title("Lab10")
        root.geometry('480x240')
        root.resizable(False, False)

    def __init_menu(self) -> None:
        stdlog('Создание меню')
        root = self.rt
        main_menu = tk.Menu(root)
        
        fl_menu = tk.Menu(main_menu, tearoff=0)
        fl_menu.add_command(label="Выход", command=self.quit)

        edit_menu = tk.Menu(main_menu, tearoff=0)
        edit_menu.add_command(label="Скрыть фамилию", command=self.hide_label)
        edit_menu.add_command(label="Показать фамилию", command=self.show_label)
        edit_menu.add_separator()

        font_menu = tk.Menu(root, tearoff=0)
        font_menu.add_command(label='Segoe UI', command=lambda: self.change_font(SEGOE_UI))
        font_menu.add_command(label='Times New Roman', command=lambda: self.change_font(TIMES_NEW_ROMAN))

        edit_menu.add_cascade(label='Сменить шрифт', menu=font_menu)

        help_menu = tk.Menu(main_menu, tearoff=0)
        help_menu.add_command(label="Помощь", command=self.show_info)

        main_menu.add_cascade(label="Файл", menu=fl_menu)
        main_menu.add_cascade(label="Редактирование", menu=edit_menu)
        main_menu.add_cascade(label="Инфо", menu=help_menu)
        root.config(menu=main_menu)

    def __init_context_menu(self) -> None:
        menu = tk.Menu(self.rt, tearoff=0)

        font_menu = tk.Menu(self.rt, tearoff=0)
        font_menu.add_command(label='Segoe UI', command=lambda: self.change_font(SEGOE_UI))
        font_menu.add_command(label='Times New Roman', command=lambda: self.change_font(TIMES_NEW_ROMAN))

        menu.add_command(label='Показать фамилию', command=self.show_label)
        menu.add_command(label='Скрыть фамилию', command=self.hide_label)
        menu.add_separator()
        menu.add_cascade(label='Сменить шрифт', menu=font_menu)
        menu.add_separator()
        menu.add_command(label='Инфо', command=self.show_info)
        menu.add_separator()
        menu.add_command(label='Выход', command=self.quit)
        
        def show_menu(e) -> None:
            menu.post(e.x_root, e.y_root)
        
        self.rt.bind("<Button-3>", show_menu)

    def change_font(self, font) -> None:
        stdlog(f'смена шрифта на \"{font[0]}\"')
        self.main_lbl.config(font=font)

    def quit(self) -> None:
        stdlog('Завершение работы программы')
        self.rt.quit()
    
    def hide_label(self) -> None:
        stdlog('Скрыта Фамилия')
        self.main_lbl.pack_forget()
    
    def show_label(self) -> None:
        stdlog('Отображена Фамилия')
        self.main_lbl.pack(pady=32)
    
    def show_info(self) -> None:
        stdlog('Отображено информационное окно')
        messagebox.showinfo("Информация о Lab10", "Это десятая лабараторная работа курса\n\"Программирование в Python\"")
        stdlog('Закрыто информационное окно')
    
# int main() // :p
if __name__ == "__main__":
    DBG = True
    app = Lab10()
import tkinter as tk
from tkinter import ttk

MAIN_FONT = "Segoe UI"

def set_font(name: str = MAIN_FONT, size: int = 9, bold: bool = False) -> tuple:
    if bold: return (name, size, 'bold')
    return (name, size)


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

class Lab11:
    def __init__(self) -> None:
        stdlog('Инициализация экземпляра класса Lab10')
        self.rt = tk.Tk()
        self.__init_tk_root()

        self.main_frame = tk.Frame(self.rt)
        self.main_frame.pack(side='top', anchor='n', fill='both')

        self.table_frame = tk.Frame(self.main_frame, bd=2, relief='sunken')
        self.table_frame.grid(row=0, column=0, padx=5, pady=5)

        self.labels_lst = list()
        self.__init_grid_labels()

        # self.l_change_text(self.labels_lst[0][0], 'Help me please!')
        
        self.tbl_select_frame_main = tk.Frame(self.main_frame)
        self.tbl_select_frame_main.grid(row=0, column=1)

        self.tbl_select_frame_up = tk.Frame(self.tbl_select_frame_main)
        self.tbl_select_frame_up.pack(side='top',anchor='nw', fill='both')
        
        self.col_lbl = tk.Label(self.tbl_select_frame_up, text="Столбец", font=set_font(), anchor='w')
        self.col_lbl.grid(row=0, column=0, padx=5)

        self.col_num_sb = ttk.Spinbox(self.tbl_select_frame_up, from_=1, to=4, increment=1, width=2, font=set_font(size=10))
        self.col_num_sb.grid(row=0, column=1)
        
        self.row_lbl = tk.Label(self.tbl_select_frame_up, text="Строка", font=set_font(), anchor='w')
        self.row_lbl.grid(row=1, column=0, padx=5)

        self.row_num_sb = ttk.Spinbox(self.tbl_select_frame_up, from_=1, to=5, increment=1, width=2, font=set_font(size=10))
        self.row_num_sb.grid(row=1, column=1)

        self.tbl_select_frame_down = tk.Frame(self.tbl_select_frame_main)
        self.tbl_select_frame_down.pack(side='top', anchor='nw', fill='both')

        self.entry = ttk.Entry(self.tbl_select_frame_down, width=16, font=set_font())
        # self.entry.pack(side='top', anchor='nw', padx=3, pady=8)
        self.entry.grid(row=0, column=0, padx=3, pady=16)

        self.entry_btn = ttk.Button(self.tbl_select_frame_down, text='Занесение', command=self.set_label_value)
        # self.entry_btn.pack(side='top', anchor='nw', padx=3, pady=2)
        self.entry_btn.grid(row=0, column=1, padx=3)


        self.close_btn = ttk.Button(self.rt, text='Закрыть', command=self.quit)
        self.close_btn.pack(side='bottom', anchor='se', padx=6, pady=4)

        self.rt.mainloop()

    def __init_grid_labels(self) -> None:
        for rows in range(0, 5):
            row = []
            for cols in range(0,4):
                lbl = tk.Label(self.table_frame,text=f"{rows}{cols}", font=set_font(), padx=2, pady=2, width=6, height=1)
                lbl.grid(row=rows, column=cols)
                row += [lbl]
            self.labels_lst += [row]

    def set_label_value(self) -> None:
        try:
            col = int(self.col_num_sb.get()) - 1
            row = int(self.row_num_sb.get()) - 1

            dat = str(self.entry.get())

            if col != None and row != None and dat != None:
                self.l_change_text(self.labels_lst[row][col], dat)
        except: pass

    def __init_tk_root(self) -> None:
        stdlog('Инициализация tkinter.root')
        root = self.rt
        root.title("Lab11")
        # root.geometry('480x240')
        # root.resizable(False, False)

    def l_change_text(self, lbl, new_text: str = '') -> None:
        lbl.config(text=new_text)

    def quit(self) -> None:
        self.rt.quit()

    pass

# int main() // :p
if __name__ == "__main__":
    app = Lab11()
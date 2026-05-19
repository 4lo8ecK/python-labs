import tkinter as tk
from tkinter import ttk

MAIN_FONT = "Segoe UI"

class Lab9:
    def __init__(self) -> None:
        self.rt = tk.Tk()
        self.rt.title("Lab9")
        
        self.width = 30
        self.height = 10
        self.min_width = 5
        self.min_height = 5

        self.__init_text()
        self.__init_step_comb()
        self.__init_buttons()

        self.update_display()
        self.rt.mainloop()

    def __init_text(self) -> None:
        self.text_frame = tk.Frame(self.rt)
        self.text_frame.pack(expand=True, fill='both', pady=10)

        self.text_area = tk.Text(self.text_frame, width=self.width, height=self.height, font=(MAIN_FONT, 14))
        self.text_area.pack()
        
        self.ctrl_frame = tk.Frame(self.rt)
        self.ctrl_frame.pack(pady=10)

        tk.Label(self.ctrl_frame, text="Шаг:").grid(row=0, column=0)

    def __init_step_comb(self) -> None:
        self.step_comb = ttk.Combobox(self.ctrl_frame, values=[1, 2, 3], width=3, state="readonly")
        self.step_comb.current(0)
        self.step_comb.grid(row=0, column=1, padx=10)

    def __init_buttons(self) -> None:
        self.btn_up     = ttk.Button(self.ctrl_frame, text="↑", width=5, command=lambda: self.resize(0, -1))
        self.btn_down   = ttk.Button(self.ctrl_frame, text="↓", width=5, command=lambda: self.resize(0, 1))
        self.btn_left   = ttk.Button(self.ctrl_frame, text="←", width=5, command=lambda: self.resize(-1, 0))
        self.btn_right  = ttk.Button(self.ctrl_frame, text="→", width=5, command=lambda: self.resize(1, 0))

        self.btn_up.grid(row=0, column=3)
        self.btn_left.grid(row=1, column=2)
        self.btn_down.grid(row=1, column=3)
        self.btn_right.grid(row=1, column=4)

        ttk.Button(self.rt, text="Close", command=self.rt.destroy).pack(pady=5) 

    def resize(self, x, y) -> None:
        step = int(self.step_comb.get())
        
        new_width = self.width + (x * step)
        new_height = self.height + (y * step)

        if new_width >= self.min_width:
            self.width = new_width
            self.btn_up.grid()
        else:
            self.btn_up.grid_remove()
        
        if new_height >= self.min_height:
            self.height = new_height
            self.btn_left.grid()
        else:
            self.btn_left.grid_remove()
            
        self.update_display()

    def update_display(self) -> None:
        self.text_area.config(width=self.width, height=self.height)
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert("1.0", f"Размер: {self.width}x{self.height}")

        if self.width <= self.min_width:
            self.btn_left.grid_remove()
        else:
            self.btn_left.grid()

        if self.height <= self.min_height:
            self.btn_up.grid_remove()
        else:
            self.btn_up.grid()

# int main() // :P
if __name__ == "__main__":
    app = Lab9()
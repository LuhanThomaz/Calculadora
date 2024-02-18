import tkinter as tk
from tkinter import ttk

class Calculadora:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.texto_da_equacao = ""


        self.display = tk.Text(root, height=2, width=16, font=("Arial", 24), bd=0, bg="#f5f5f5")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.create_buttons()

    def create_buttons(self):

        button_color = "#e1e1e1"
        button_active_color = "#c1c1c1"
        text_color = "#000000"
        button_padx = 10
        button_pady = 10
        button_style = {"font": ("Arial", 24, "bold"), "bd": 1, "bg": button_color, "fg": text_color, "activebackground": button_active_color}

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
            ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
            ('=', 4, 2), ('C', 4, 0),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, **button_style, width=4, height=1)
            button.grid(row=row, column=col, padx=button_padx, pady=button_pady, sticky="nsew")
            button.bind('<Button-1>', self.click)


    
    def click(self, event):
        text = event.widget.cget("text")
        if text == "=":
            try:
                result = str(eval(self.texto_da_equacao))
                self.clear()
                self.display.insert(tk.END, result)
            except Exception as e:
                self.clear()
                self.display.insert(tk.END, "Error")
        elif text == "C":
            self.clear()
        else:
            self.display.insert(tk.END, text)
            self.texto_da_equacao += text
    
    def clear(self):
        self.display.delete(1.0, tk.END)
        self.texto_da_equacao = ""

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#f5f5f5")
    calc = Calculadora(root)
    root.mainloop()

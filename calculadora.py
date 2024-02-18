import tkinter as tk
from tkinter import ttk
#Definição da classe calculadora que encapsula a lógica e a interface da calculadora
class Calculadora:
    #método construtor
    def __init__(self, root):
        #representa a instância da classe
        self.root = root
        #root é um parâmetro que aguarda um objeto TK que é a janela principal da GUI, self.root  = root armazena o objeto TK passando como root na instância da classe
        #self.root.title define o título da janela como calculadora
        self.root.title("Calculadora")


        #Inicilizando uma variável como sttring vazia para armazenar a equação que será calculada
        self.texto_da_equacao = ""


        # criação de um widget de texto que serve como display definindo as dimensões, bordas, cores e posicionamento.
        self.display = tk.Text(root, height=2, width=16, font=("Arial", 24), bd=0, bg="#f5f5f5")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.create_buttons()

    
    # cria os botões definindo as cores, estilo e dimensões.
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


    #método que define a lógica quando ocorre o click em algum  botão e captura o texto ou valor do botão pressionado.
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
    #Função que Limpa o display e a variável self.texto_da_equacao
    def clear(self):
        self.display.delete(1.0, tk.END)
        self.texto_da_equacao = ""

#criação da execução da calculadora
if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#f5f5f5")
    calc = Calculadora(root)
    root.mainloop()

import tkinter as tk
import math

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("350x350")
        self.master.configure(bg="#F0F0F0")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.entry = tk.Entry(master, textvariable=self.result_var, font=('Helvetica', 20), bd=10, insertwidth=4, width=14, justify="center")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ('C', 4, 2), ('.', 4, 1), ('√', 5, 0), ('=', 5, 1),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            tk.Button(master, text=text, command=lambda t=text: self.on_button_click(t), font=('Helvetica', 15), bd=5, padx=20, pady=20).grid(row=row, column=col)

        # Configure row and column weights to make the calculator resize properly
        for i in range(6):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == 'C':
            self.result_var.set('')
        elif button_text == '=':
            try:
                result = eval(current_text)
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set('Error')
        elif button_text == '√':
            try:
                result = math.sqrt(float(current_text))
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set('Error')
        else:
            self.result_var.set(current_text + button_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

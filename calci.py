import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x600")
        
        self.expression = ""
        self.input_text = tk.StringVar()
        
        # Create a frame for the input field
        input_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE)
        input_frame.pack(side=tk.TOP)
        
        # Create an input field inside the frame
        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, bd=10, insertwidth=4, width=14, justify='right')
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=20)
        
        # Create buttons
        buttons_frame = tk.Frame(self.root, bd=10, relief=tk.RIDGE)
        buttons_frame.pack()
        
        # Define button labels
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '√',
            '1', '2', '3', '-', '^',
            '0', '.', '=', '+', 'M+'
        ]
        
        # Create and place buttons in the frame
        row = 0
        col = 0
        for button in buttons:
            action = lambda x=button: self.click(x)
            tk.Button(buttons_frame, text=button, font=('arial', 18, 'bold'), fg='black', bd=4, command=action).grid(row=row, column=col, padx=10, pady=10)
            col += 1
            if col > 4:
                col = 0
                row += 1
                
        # Memory storage
        self.memory = 0
    
    def click(self, item):
        try:
            if item == 'C':
                self.expression = ""
            elif item == '=':
                self.expression = str(eval(self.expression))
            elif item == '√':
                self.expression = str(math.sqrt(eval(self.expression)))
            elif item == '^':
                self.expression += '**'
            elif item == 'M+':
                self.memory += eval(self.expression)
                self.expression = str(self.memory)
            else:
                self.expression += str(item)
            
            self.input_text.set(self.expression)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            self.expression = ""
            self.input_text.set(self.expression)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.expression = ""
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox
import math

# Function to evaluate a basic arithmetic expression
def evaluate_expression(expression):
    try:
        return eval(expression)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        return ""

# Function to solve quadratic equation
def solve_quadratic(a, b, c):
    disc = b ** 2 - 4 * a * c
    if disc < 0:
        return "No Real Roots"
    sqrt_disc = math.sqrt(disc)
    root1 = (-b + sqrt_disc) / (2 * a)
    root2 = (-b - sqrt_disc) / (2 * a)
    return f"Roots: {root1}, {root2}"

# Function for button click
def on_button_click(char):
    if char == '=':
        result.set(evaluate_expression(expression.get()))
    elif char == 'Solve Quadratic':
        try:
            a = float(a_entry.get())
            b = float(b_entry.get())
            c = float(c_entry.get())
            result.set(solve_quadratic(a, b, c))
        except ValueError:
            messagebox.showerror("Error", "Invalid Input for Quadratic")
    else:
        expression.set(expression.get() + char)

# Main window setup
root = tk.Tk()
root.title("Tekso Calculator")

# Expression entry and result
expression = tk.StringVar()
result = tk.StringVar()
tk.Entry(root, textvariable=expression, width=25).grid(row=0, column=0, columnspan=4)
tk.Entry(root, textvariable=result, width=25).grid(row=1, column=0, columnspan=4)

# Numeric and operation buttons
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', 'C', '=', '/'
]
row = 2
col = 0
for char in buttons:
    button = tk.Button(root, text=char, command=lambda ch=char: on_button_click(ch))
    button.grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Quadratic equation inputs
a_entry = tk.Entry(root, width=5)
a_entry.grid(row=6, column=0)
b_entry = tk.Entry(root, width=5)
b_entry.grid(row=6, column=1)
c_entry = tk.Entry(root, width=5)
c_entry.grid(row=6, column=2)
quad_button = tk.Button(root, text="Solve Quadratic", command=lambda: on_button_click("Solve Quadratic"))
quad_button.grid(row=6, column=3)

root.mainloop()

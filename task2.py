import numpy as np
import tkinter as tk
from tkinter import ttk


# Define the function and its derivative
def f(x):
    return x ** 2 - 4 * np.sin(x)


def df(x):
    return 2 * x - 4 * np.cos(x)


# False Position Method
def false_position(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("Function must have opposite signs at a and b")

    iter_count = 0
    c = a  # Initial guess
    for _ in range(max_iter):
        c_old = c
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        iter_count += 1

        if abs(f(c)) < tol or abs(c - c_old) < tol:
            return c, iter_count, abs((c - c_old) / c) if c != 0 else 0

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c, iter_count, abs((c - c_old) / c) if c != 0 else 0


# Newton-Raphson Method
def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    iter_count = 0
    for _ in range(max_iter):
        x_new = x - f(x) / df(x)
        iter_count += 1
        if abs(x_new - x) < tol:
            return x_new, iter_count, abs((x_new - x) / x_new) if x_new != 0 else 0
        x = x_new
    return x, iter_count, abs((x_new - x) / x_new) if x_new != 0 else 0


# Function to display Task 2 inputs and results
def show_task2_inputs(frame):
    # Clear previous widgets
    for widget in frame.winfo_children():
        widget.destroy()

    # Configure styles
    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 15), background="#baf6ff")
    style.configure("TButton", font=("Arial", 15), padding=6)
    style.configure("TEntry", font=("Arial", 15), padding=5)
    style.configure("TCombobox", font=("Arial", 15), padding=5)

    # Input fields for interval [a, b]
    ttk.Label(frame, text="Interval [a, b]:").pack(pady=5)
    entry_a = ttk.Entry(frame)
    entry_a.pack(pady=5)
    entry_b = ttk.Entry(frame)
    entry_b.pack(pady=5)

    # Input field for initial guess (Newton-Raphson)
    ttk.Label(frame, text="Initial Guess x0 (for Newton-Raphson):").pack(pady=5)
    entry_x0 = ttk.Entry(frame)
    entry_x0.pack(pady=5)

    # Dropdown to select method
    method_var = tk.StringVar(value='False Position')
    method_menu = ttk.Combobox(frame, textvariable=method_var, values=['False Position', 'Newton-Raphson'])
    method_menu.pack(pady=5)

    # Function to calculate the root
    def calculate_root():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            x0 = float(entry_x0.get()) if entry_x0.get() else 0

            if method_var.get() == 'False Position':
                root, iterations, rel_error = false_position(f, a, b)
            else:
                root, iterations, rel_error = newton_raphson(f, df, x0)

            result_label.config(text=f"Root: {root:.6f}\nIterations: {iterations}\nRelative Error: {rel_error:.6e}")
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")

    # Button to trigger calculation
    ttk.Button(frame, text="Calculate Root", command=calculate_root).pack(pady=10)

    # Label to display results
    result_label = ttk.Label(frame, text="Result: ")
    result_label.pack(pady=5)

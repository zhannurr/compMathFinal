import numpy as np
import tkinter as tk
from tkinter import ttk

def f2(x):
    return x**2 - 4*np.sin(x)

def df2(x):
    return 2*x - 4*np.cos(x)

def false_position(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("Function must have opposite signs at a and b")
    
    for _ in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

def show_task2_inputs(frame):
    ttk.Label(frame, text="Interval [a, b]:").grid(row=0, column=0)
    entry_a = ttk.Entry(frame)
    entry_a.grid(row=0, column=1)
    entry_b = ttk.Entry(frame)
    entry_b.grid(row=0, column=2)
    
    ttk.Label(frame, text="Initial Guess x0:").grid(row=1, column=0)
    entry_x0 = ttk.Entry(frame)
    entry_x0.grid(row=1, column=1)
    
    method_var = tk.StringVar(value='False Position')
    method_menu = ttk.Combobox(frame, textvariable=method_var, values=['False Position', 'Newton-Raphson'])
    method_menu.grid(row=2, column=1)
    
    def calculate_root():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            x0 = float(entry_x0.get())
            
            if method_var.get() == 'False Position':
                root = false_position(f2, a, b)
            else:
                root = newton_raphson(f2, df2, x0)
            
            result_label.config(text=f"Root: {root:.6f}")
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")
    
    ttk.Button(frame, text="Calculate Root", command=calculate_root).grid(row=3, column=1)
    result_label = ttk.Label(frame, text="Result: ")
    result_label.grid(row=4, column=1)
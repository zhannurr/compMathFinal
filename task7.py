import numpy as np
import tkinter as tk
from tkinter import ttk

def taylor_series_method(x0, y0, x, n=3):
    """
    Solves the differential equation dy/dx = y^2 + x^2 using Taylor series up to the third derivative.
    """
    h = x - x0
    
    f = lambda x, y: y**2 + x**2
    f1 = lambda x, y: 2 * y * f(x, y) + 2 * x  # First derivative
    f2 = lambda x, y: 2 * (f(x, y) * f1(x, y) + y * f1(x, y) + 1)  # Second derivative
    f3 = lambda x, y: 2 * (f(x, y) * f2(x, y) + f1(x, y)**2 + y * f2(x, y))  # Third derivative
    
    y_approx = y0 + h * f(x0, y0) + (h**2 / 2) * f1(x0, y0) + (h**3 / 6) * f2(x0, y0)
    
    return y_approx

def show_task7_inputs(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    
    ttk.Label(frame, text="Enter initial condition y(0) =", font=("Arial", 15)).grid(row=0, column=0, padx=5, pady=5)
    y0_entry = ttk.Entry(frame, width=10, font=("Arial", 15))
    y0_entry.grid(row=0, column=1, padx=5, pady=5)
    y0_entry.insert(0, "1")
    
    ttk.Label(frame, text="Compute y at x =", font=("Arial", 15)).grid(row=1, column=0, padx=5, pady=5)
    x_entry = ttk.Entry(frame, width=10, font=("Arial", 15))
    x_entry.grid(row=1, column=1, padx=5, pady=5)
    
    result_label = ttk.Label(frame, text="Result: ", font=("Arial", 15))
    result_label.grid(row=3, column=0, columnspan=2, pady=10)
    
    def calculate_taylor():
        try:
            y0 = float(y0_entry.get())
            x = float(x_entry.get())
            y_result = taylor_series_method(0, y0, x)
            result_label.config(text=f"y({x}) ≈ {y_result:.6f}")
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")
    
    ttk.Button(frame, text="Calculate", command=calculate_taylor).grid(row=2, column=0, columnspan=2, pady=10)

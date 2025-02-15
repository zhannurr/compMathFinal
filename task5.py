import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def linear_least_squares(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    num = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    den = sum((x[i] - x_mean) ** 2 for i in range(n))
    
    m = num / den
    b = y_mean - m * x_mean
    
    return m, b

def show_task5_inputs(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    
    ttk.Label(frame, text="Linear Curve Fitting", font=("Arial", 15), background="#baf6ff").pack(pady=10)
    
    ttk.Label(frame, text="Enter X values (comma separated):", font=("Arial", 12), background="#baf6ff").pack()
    x_entry = ttk.Entry(frame, font=("Arial", 12))
    x_entry.pack(pady=5)
    
    ttk.Label(frame, text="Enter Y values (comma separated):", font=("Arial", 12), background="#baf6ff").pack()
    y_entry = ttk.Entry(frame, font=("Arial", 12))
    y_entry.pack(pady=5)
    
    result_label = ttk.Label(frame, text="Result: ", font=("Arial", 15), background="#baf6ff")
    result_label.pack(pady=10)
    
    def calculate_fit():
        try:
            x_values = list(map(float, x_entry.get().split(',')))
            y_values = list(map(float, y_entry.get().split(',')))
            if len(x_values) != len(y_values):
                result_label.config(text="Error: X and Y must have the same length")
                return
            
            m, b = linear_least_squares(x_values, y_values)
            result_label.config(text=f"Equation: y = {m:.4f}x + {b:.4f}")
            plot_graph(x_values, y_values, m, b)
        except ValueError:
            result_label.config(text="Error: Invalid input")
    
    ttk.Button(frame, text="Calculate Fit", command=calculate_fit, style="TButton").pack(pady=10)

def plot_graph(x, y, m, b):
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.scatter(x, y, color='red', label='Data Points')
    
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = m * x_fit + b
    ax.plot(x_fit, y_fit, color='blue', label='Best Fit Line')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Linear Curve Fitting')
    ax.legend()
    
    for widget in plot_frame.winfo_children():
        widget.destroy()
    
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
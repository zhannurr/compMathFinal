import numpy as np
import tkinter as tk
from tkinter import ttk

def jacobi_method(A, b, x0=None, tol=1e-6, max_iter=100):
    n = len(b)
    x = np.zeros(n) if x0 is None else np.array(x0, dtype=float)
    x_new = np.zeros(n)
    
    for _ in range(max_iter):
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum1) / A[i][i]
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new.copy()
    
    return x_new

def show_task3_inputs(frame):
    ttk.Label(frame, text="Initial Guess [x0, y0, z0]:").grid(row=0, column=0)
    entry_x0 = ttk.Entry(frame)
    entry_x0.grid(row=0, column=1)
    entry_y0 = ttk.Entry(frame)
    entry_y0.grid(row=0, column=2)
    entry_z0 = ttk.Entry(frame)
    entry_z0.grid(row=0, column=3)
    
    def calculate_jacobi():
        try:
            x0 = [float(entry_x0.get()), float(entry_y0.get()), float(entry_z0.get())]
            A = np.array([[3, 1, -1], [2, -8, 1], [-1, 1, 5]], dtype=float)
            b = np.array([1, -2, 3], dtype=float)
            solution = jacobi_method(A, b, x0)
            result_label.config(text=f"Solution: {solution}")
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")
    
    ttk.Button(frame, text="Solve", command=calculate_jacobi).grid(row=1, column=1)
    result_label = ttk.Label(frame, text="Result: ")
    result_label.grid(row=2, column=1)

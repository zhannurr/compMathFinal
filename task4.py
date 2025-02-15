import numpy as np
import tkinter as tk
from tkinter import ttk

def iterative_matrix_inversion(A, tol=1e-6, max_iter=100):
    n = A.shape[0]
    I = np.eye(n)
    
    # Initial guess: (1 / trace(A)) * I
    trace_A = np.trace(A)
    if trace_A == 0:
        raise ValueError("Matrix trace is zero, cannot compute initial guess.")
    X = (1 / trace_A) * I
    
    for _ in range(max_iter):
        X_new = X @ (2 * I - A @ X)
        
        # Convergence check: ||AX - I||
        if np.linalg.norm(A @ X_new - I, ord=np.inf) < tol:
            return X_new
        X = X_new
    
    return X

def show_task4_inputs(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    
    ttk.Label(frame, text="Enter matrix values:", font=("Arial", 12), background="#baf6ff").grid(row=0, column=0, columnspan=4, pady=5)
    
    size = 3  # Default size of matrix (3x3)
    entries = []
    for i in range(size):
        row_entries = []
        for j in range(size):
            entry = ttk.Entry(frame, width=5, font=("Arial", 12))
            entry.grid(row=i+1, column=j, padx=5, pady=5)
            row_entries.append(entry)
        entries.append(row_entries)
    
    result_label = ttk.Label(frame, text="Result: ", font=("Arial", 15), background="#baf6ff")
    result_label.grid(row=size+2, column=0, columnspan=4, pady=10)
    
    def calculate_inverse():
        try:
            A = np.array([[float(entries[i][j].get()) for j in range(size)] for i in range(size)], dtype=float)
            
            A_inv = iterative_matrix_inversion(A)
            result_label.config(text=f"Inverse Matrix:\n{A_inv}")
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")
    
    ttk.Button(frame, text="Compute Inverse", command=calculate_inverse, style="TButton").grid(row=size+1, column=0, columnspan=4, pady=10)

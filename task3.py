import numpy as np
import tkinter as tk
from tkinter import ttk


def jacobi_method(A, b, x0=None, tol=1e-6, max_iter=100):
    n = len(b)
    x = np.zeros(n) if x0 is None else np.array(x0, dtype=float)

    for _ in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum1) / A[i][i]

        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new

    return x_new


def show_task3_inputs(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text="Enter coefficients for 3x3 system:", font=("Arial", 15), background="#baf6ff").grid(row=0,
                                                                                                               column=0,
                                                                                                               columnspan=4,
                                                                                                               pady=10)

    entries = []
    for i in range(3):
        row_entries = []
        for j in range(3):
            entry = ttk.Entry(frame, width=5, font=("Arial", 15))
            entry.grid(row=i + 1, column=j, padx=5, pady=5)
            row_entries.append(entry)
        entries.append(row_entries)

        b_entry = ttk.Entry(frame, width=5, font=("Arial", 15))
        b_entry.grid(row=i + 1, column=3, padx=5, pady=5)
        row_entries.append(b_entry)

    ttk.Label(frame, text="Initial Guess [x0, y0, z0]:", font=("Arial", 15), background="#baf6ff").grid(row=4, column=0,
                                                                                                        columnspan=3,
                                                                                                        pady=10)

    entry_x0 = ttk.Entry(frame, width=10, font=("Arial", 15))
    entry_x0.grid(row=5, column=0, padx=5, pady=5)
    entry_y0 = ttk.Entry(frame, width=10, font=("Arial", 15))
    entry_y0.grid(row=5, column=1, padx=5, pady=5)
    entry_z0 = ttk.Entry(frame, width=10, font=("Arial", 15))
    entry_z0.grid(row=5, column=2, padx=5, pady=5)

    result_label = ttk.Label(frame, text="Result: ", font=("Arial", 15), background="#baf6ff")
    result_label.grid(row=7, column=0, columnspan=4, pady=10)

    def calculate_jacobi():
        try:
            A = np.array([[float(entries[i][j].get()) for j in range(3)] for i in range(3)], dtype=float)
            b = np.array([float(entries[i][3].get()) for i in range(3)], dtype=float)
            x0 = [float(entry_x0.get()), float(entry_y0.get()), float(entry_z0.get())]
            solution = jacobi_method(A, b, x0)
            result_label.config(text=f"Solution: x = {solution[0]:.4f}, y = {solution[1]:.4f}, z = {solution[2]:.4f}")
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")

    ttk.Button(frame, text="Solve", command=calculate_jacobi, style="TButton").grid(row=6, column=0, columnspan=4,
                                                                                    pady=10)

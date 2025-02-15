import numpy as np
import tkinter as tk
from tkinter import ttk


def iterative_matrix_inversion(A, tol=1e-6, max_iter=100):
    n = A.shape[0]  # Get the matrix size
    I = np.eye(n)  # Create an identity matrix of the same size

    # Initial guess: (1 / trace(A)) * I
    trace_A = np.trace(A)
    if trace_A == 0:
        raise ValueError("Matrix trace is zero, cannot compute initial guess.")
    X = (1 / trace_A) * I  # Initial inverse matrix

    for _ in range(max_iter):
        X_new = X @ (2 * I - A @ X)  # Main formula of the Newton-Schulz method

        # Convergence check: ||AX - I|| (infinity norm)
        if np.linalg.norm(A @ X_new - I, ord=np.inf) < tol:
            return X_new
        X = X_new  # Update X

    return X  # Return the approximated inverse matrix


# Function to display matrix input and compute its inverse

def show_task4_inputs(frame):
    for widget in frame.winfo_children():  # Clear the frame before rendering
        widget.destroy()

    ttk.Label(frame, text="Enter matrix values:", font=("Arial", 12), background="#baf6ff").grid(row=0, column=0,
                                                                                                 columnspan=4, pady=5)

    size = 3  # Default matrix size (3x3)
    entries = []  # List to store input fields
    for i in range(size):
        row_entries = []
        for j in range(size):
            entry = ttk.Entry(frame, width=5, font=("Arial", 12))  # Create input field
            entry.grid(row=i + 1, column=j, padx=5, pady=5)
            row_entries.append(entry)
        entries.append(row_entries)

    result_label = ttk.Label(frame, text="Result: ", font=("Arial", 15), background="#baf6ff")
    result_label.grid(row=size + 2, column=0, columnspan=4, pady=10)

    # Function to compute the inverse matrix from user input
    def calculate_inverse():
        try:
            # Read input fields and form matrix A
            A = np.array([[float(entries[i][j].get()) for j in range(size)] for i in range(size)], dtype=float)

            # Compute the inverse matrix using the iterative method
            A_inv = iterative_matrix_inversion(A)
            result_label.config(text=f"Inverse Matrix:\n{A_inv}")  # Display the result
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")  # Display an error message if something goes wrong

    # Button to start the computation
    ttk.Button(frame, text="Compute Inverse", command=calculate_inverse, style="TButton").grid(row=size + 1, column=0,
                                                                                               columnspan=4, pady=10)

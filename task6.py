import numpy as np
from tkinter import ttk


# Function to compute first derivative using Newton’s Forward Difference Formula
def newtons_forward_difference(x, y, x_target):
    h = x[1] - x[0]  # Step size
    dy_dx = (y[1] - y[0]) / h + ((y[2] - 2 * y[1] + y[0]) / (2 * h))  # Formula for first derivative
    return dy_dx


# Function to display input fields for Task 6
def show_task6_inputs(frame):
    """Creates UI elements to input values for Newton’s Forward Difference Formula."""
    for widget in frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text="Newton’s Forward Difference Formula", font=("Arial", 15), background="#baf6ff").pack(pady=10)
    ttk.Label(frame, text="Enter X values (comma separated):", font=("Arial", 12), background="#baf6ff").pack()
    x_entry = ttk.Entry(frame, font=("Arial", 12))
    x_entry.pack(pady=5)

    ttk.Label(frame, text="Enter Y values (comma separated):", font=("Arial", 12), background="#baf6ff").pack()
    y_entry = ttk.Entry(frame, font=("Arial", 12))
    y_entry.pack(pady=5)

    ttk.Label(frame, text="Enter Target X:", font=("Arial", 12), background="#baf6ff").pack()
    x_target_entry = ttk.Entry(frame, font=("Arial", 12))
    x_target_entry.pack(pady=5)

    result_label = ttk.Label(frame, text="Result: ", font=("Arial", 15), background="#baf6ff")
    result_label.pack(pady=10)

    # Function to compute the first derivative
    def calculate_forward_difference():
        """Handles input parsing, error checking, and derivative computation."""
        try:
            x_values = list(map(float, x_entry.get().split(',')))
            y_values = list(map(float, y_entry.get().split(',')))
            x_target = float(x_target_entry.get())

            if len(x_values) < 3 or len(y_values) < 3:
                result_label.config(text="Error: Need at least 3 data points")
                return

            # Compute the derivative using Newton’s Forward Difference Formula
            result = newtons_forward_difference(np.array(x_values), np.array(y_values), x_target)
            result_label.config(text=f"First Derivative at x={x_target}: {result:.6f}")
        except ValueError:
            result_label.config(text="Error: Invalid input")

    ttk.Button(frame, text="Compute Derivative", command=calculate_forward_difference, style="TButton").pack(pady=10)
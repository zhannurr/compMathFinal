import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk


# Function to compute integral using Simpson’s 3/8 Rule
def simpsons_three_eighth_rule(f, a, b, n):
    """Approximates the integral of f(x) from a to b using Simpson's 3/8 Rule with n subintervals."""
    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3")

    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    y = f(x)

    integral = (3 * h / 8) * (y[0] + 3 * sum(y[1:n:3]) + 3 * sum(y[2:n:3]) + 2 * sum(y[3:n - 1:3]) + y[n])
    return integral, x, y


def f(x):
    """Defines the function to integrate: f(x) = x^3."""
    return x ** 3


# Function to display input fields for Task 8
def show_task8_inputs(frame):
    """Creates UI elements to input values for Simpson’s 3/8 Rule integration."""
    for widget in frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text="Simpson’s 3/8 Rule", font=("Arial", 15), background="#baf6ff").pack(pady=10)
    ttk.Label(frame, text="Enter Lower Limit (a):", font=("Arial", 12), background="#baf6ff").pack()
    a_entry = ttk.Entry(frame, font=("Arial", 12))
    a_entry.pack(pady=5)

    ttk.Label(frame, text="Enter Upper Limit (b):", font=("Arial", 12), background="#baf6ff").pack()
    b_entry = ttk.Entry(frame, font=("Arial", 12))
    b_entry.pack(pady=5)

    ttk.Label(frame, text="Enter Number of Intervals (n, multiple of 3):", font=("Arial", 12),
              background="#baf6ff").pack()
    n_entry = ttk.Entry(frame, font=("Arial", 12))
    n_entry.pack(pady=5)

    result_label = ttk.Label(frame, text="Result: ", font=("Arial", 15), background="#baf6ff")
    result_label.pack(pady=10)

    compute_button = ttk.Button(frame, text="Compute Integral")
    compute_button.pack(pady=10)

    def calculate_simpsons_three_eighth_rule():
        """Handles input parsing, error checking, calculation, and visualization of the integral."""
        try:
            a = float(a_entry.get())
            b = float(b_entry.get())
            n = int(n_entry.get())

            if n % 3 != 0:
                result_label.config(text="Error: n must be a multiple of 3.")
                return

            approx_integral, x_vals, y_vals = simpsons_three_eighth_rule(f, a, b, n)
            exact_integral = (b ** 4 / 4) - (a ** 4 / 4)  # Exact integral of x^3 from a to b
            absolute_error = abs(exact_integral - approx_integral)

            result_label.config(
                text=f"Approximate Integral: {approx_integral:.6f}\nAbsolute Error: {absolute_error:.6f}")

        except ValueError:
            result_label.config(text="Error: Invalid input")

    compute_button.config(command=calculate_simpsons_three_eighth_rule)

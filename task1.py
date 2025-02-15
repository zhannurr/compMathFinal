from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def f1(x):
    return np.cos(x) - x


def plot_graph(frame, a, b):
    # for widget in frame.winfo_children():
    #    widget.destroy()
    """Plots the function f(x) = cos(x) - x over the user-defined interval [a, b]
    and marks the approximate root found using the graphical method."""
    x_vals = np.linspace(a, b, 100)
    y_vals = f1(x_vals)

    # Bisection method for numerical root
    numerical_root = bisect(f1, a, b)

    # Approximate root from graphical method (visually estimated)
    approx_root = (a + b) / 2

    # Absolute error calculation
    absolute_error = abs(numerical_root - approx_root)

    # Create figure
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(x_vals, y_vals, label='f(x) = cos(x) - x', color='blue')
    ax.axhline(0, color='purple', linewidth=1, linestyle='--')
    ax.scatter(numerical_root, f1(numerical_root), color='red', label=f'Numerical Root: {numerical_root:.5f}')
    ax.scatter(approx_root, f1(approx_root), color='green', label=f'Approx. Root: {approx_root:.5f}')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Graphical Method for Root Finding')
    ax.legend()
    ax.grid()

    # Display graph in Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack()
    canvas.draw()

    # Display results
    result_label = ttk.Label(frame, text=f"Numerical Root: {numerical_root:.5f}\n"
                                         f"Approx. Root: {approx_root:.5f}\n"
                                         f"Absolute Error: {absolute_error:.5f}",
                             font=("Arial", 12), background="#baf6ff")
    result_label.pack(pady=10)


def show_task1_inputs(frame):

    """Creates UI elements for user input to define the interval [a, b]."""


    ttk.Label(frame, text="Graphical Method for Root Finding", font=("Arial", 15), background="#baf6ff").pack(pady=10)

    ttk.Label(frame, text="Enter Lower Bound (a):", font=("Arial", 12), background="#baf6ff").pack()
    a_entry = ttk.Entry(frame, font=("Arial", 12))
    a_entry.pack(pady=5)

    ttk.Label(frame, text="Enter Upper Bound (b):", font=("Arial", 12), background="#baf6ff").pack()
    b_entry = ttk.Entry(frame, font=("Arial", 12))
    b_entry.pack(pady=5)

    def on_compute():
        try:
            a = float(a_entry.get())
            b = float(b_entry.get())
            if a >= b:
                raise ValueError("Lower bound must be less than upper bound.")
            plot_graph(frame, a, b)
        except ValueError:
            result_label.config(text="Error: Invalid input or incorrect range.")

    compute_button = ttk.Button(frame, text="Compute Graph", command=on_compute)
    compute_button.pack(pady=10)

    result_label = ttk.Label(frame, text="", font=("Arial", 12), background="#baf6ff")
    result_label.pack(pady=10)

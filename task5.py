import numpy as np
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Function to compute the coefficients of linear regression using the least squares method
def linear_least_squares(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Compute numerator and denominator for slope (m)
    num = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    den = sum((x[i] - x_mean) ** 2 for i in range(n))

    m = num / den  # Slope of the line
    b = y_mean - m * x_mean  # Intercept (Y-axis crossing point)

    return m, b


def show_task5_inputs(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    ttk.Label(frame, text="Linear Curve Fitting", font=("Arial", 15), background="#baf6ff").pack(pady=10)

    # Input field for X values
    ttk.Label(frame, text="Enter X values (comma separated):", font=("Arial", 12), background="#baf6ff").pack()
    x_entry = ttk.Entry(frame, font=("Arial", 12))
    x_entry.pack(pady=5)

    # Input field for Y values
    ttk.Label(frame, text="Enter Y values (comma separated):", font=("Arial", 12), background="#baf6ff").pack()
    y_entry = ttk.Entry(frame, font=("Arial", 12))
    y_entry.pack(pady=5)

    # display the result
    result_label = ttk.Label(frame, text="Result: ", font=("Arial", 15), background="#baf6ff")
    result_label.pack(pady=10)

    # Function to calculate the linear fit
    def calculate_fit():
        try:
            x_values = list(map(float, x_entry.get().split(',')))  # Convert input string to list of numbers
            y_values = list(map(float, y_entry.get().split(',')))

            # Ensure both lists have the same length
            if len(x_values) != len(y_values):
                result_label.config(text="Error: X and Y must have the same length")
                return

            # Compute the linear regression coefficients
            m, b = linear_least_squares(x_values, y_values)
            result_label.config(text=f"Equation: y = {m:.4f}x + {b:.4f}")

            plot_graph(x_values, y_values, m, b, frame)
        except ValueError:
            result_label.config(text="Error: Invalid input")

    # Button to trigger calculations
    ttk.Button(frame, text="Calculate Fit", command=calculate_fit, style="TButton").pack(pady=10)


# Function to plot the graph
def plot_graph(x, y, m, b, frame):
    fig, ax = plt.subplots(figsize=(5, 4))  # Create the figure for the plot
    ax.scatter(x, y, color='red', label='Data Points')  # Display data points

    # Generate the regression line
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = m * x_fit + b
    ax.plot(x_fit, y_fit, color='blue', label='Best Fit Line')

    # Configure plot labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Linear Curve Fitting')
    ax.legend()

    # Clear previous graph and display the new one
    # for widget in frame.winfo_children():
    #     widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

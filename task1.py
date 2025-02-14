import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect


def f1(x):
    return np.cos(x) - x


def plot_graph():
    # Plots the function f(x) = cos(x) - x over the interval [0,1]
    # and marks the approximate root found using the graphical method.
    x_vals = np.linspace(0, 1, 100)
    y_vals = f1(x_vals)

    # bisection method
    numerical_root = bisect(f1, 0, 1)

    # Approximate root from graphical method (visually estimated)
    approx_root = 0.75

    # Absolute error calculation
    absolute_error = abs(numerical_root - approx_root)

    # Plot the function
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label='f(x) = cos(x) - x', color='blue')
    plt.axhline(0, color='purple', linewidth=1, linestyle='--')
    plt.scatter(numerical_root, f1(numerical_root), color='red', label=f'Numerical Root: {numerical_root:.5f}')
    plt.scatter(approx_root, f1(approx_root), color='green', label=f'Approx. Root: {approx_root:.5f}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graphical Method for Root Finding')
    plt.legend()
    plt.grid()
    plt.show()

    # Print results
    print(f"Numerical Root: {numerical_root:.5f}")
    print(f"Approximate Root (Graphical): {approx_root:.5f}")
    print(f"Absolute Error: {absolute_error:.5e}")

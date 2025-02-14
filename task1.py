import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return np.cos(x) - x

def plot_graph():
    x_vals = np.linspace(0, 1, 100)
    y_vals = f1(x_vals)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label='f(x) = cos(x) - x')
    plt.axhline(0, color='black', linewidth=1)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graphical Method for Root Finding')
    plt.legend()
    plt.grid()
    plt.show()
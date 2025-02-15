import numpy as np
import matplotlib.pyplot as plt


# Task 8: Simpson's 1/3 Rule
def f(x):
    """
    Function to integrate: sin(x)
    """
    return np.sin(x)


def simpsons_rule(f, a, b, n):
    """
    Simpson's 1/3 Rule for numerical integration
    :param f: Function to integrate
    :param a: Lower limit
    :param b: Upper limit
    :param n: Number of subintervals (must be even)
    :return: Approximate integral value
    """
    if n % 2 == 1:
        raise ValueError("Number of subintervals must be even.")

    h = (b - a) / n  # Step size
    x = np.linspace(a, b, n + 1)  # Generate n+1 points
    y = f(x)  # Evaluate function at these points

    # Apply Simpson's Rule formula
    integral = (h / 3) * (y[0] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n - 1:2]) + y[n])
    return integral


def plot_function(f, a, b, n):
    """
    Plot the function and show Simpson's rule approximation.
    """
    x = np.linspace(a, b, 100)
    y = f(x)

    # Plot the function
    plt.plot(x, y, label='sin(x)', color='blue')

    # Plot the sample points
    x_nodes = np.linspace(a, b, n + 1)
    y_nodes = f(x_nodes)
    plt.scatter(x_nodes, y_nodes, color='red', label='Sample Points')

    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title("Simpson's Rule Approximation")
    plt.legend()
    plt.grid()
    plt.show()


def task6():
    # Given limits and subintervals
    a = 0
    b = np.pi
    n = 10  # Number of subintervals (must be even)

    # Compute numerical integral
    approx_integral = simpsons_rule(f, a, b, n)

    # Exact integral value
    exact_integral = 2

    # Error estimation
    error = abs(exact_integral - approx_integral)

    # Output results
    print(f"Approximate Integral: {approx_integral:.6f}")
    print(f"Exact Integral: {exact_integral:.6f}")
    print(f"Absolute Error: {error:.6f}")

    # Plot the function and Simpson's Rule approximation
    plot_function(f, a, b, n)


    # Task 6: Newton’s Forward Difference Formula
    def newtons_forward_difference(x, y, x_target):
        """
        Compute first derivative using Newton's Forward Difference Formula.
        """
        h = x[1] - x[0]
        dy_dx = (y[1] - y[0]) / h + ((y[2] - 2 * y[1] + y[0]) / (2 * h))
        return dy_dx


    # Given data points
    x_values = np.array([0, 1, 2])
    y_values = np.array([1, 3, 7])
    x_target = 1

    # Compute derivative at x=1
    first_derivative = newtons_forward_difference(x_values, y_values, x_target)
    print("\nTask 6: Newton’s Forward Difference Formula")
    print(f"First Derivative at x={x_target}: {first_derivative:.6f}")
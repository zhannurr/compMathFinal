def taylor_series_method(x, y, step, order=3):
    """
    Use Taylor Series expansion to compute y(x + step) using up to the third derivative.
    """
    y_deriv1 = y ** 2 + x ** 2
    y_deriv2 = 2 * y * y_deriv1 + 2 * x
    y_deriv3 = 2 * (y_deriv1 ** 2 + y * y_deriv2) + 2

    y_next = y + step * y_deriv1 + (step ** 2 / 2) * y_deriv2 + (step ** 3 / 6) * y_deriv3
    return y_next

# Initial condition
def task7():
    y_0 = 1

    # Compute y(0.1) and y(0.2)
    y_01 = taylor_series_method(0, y_0, 0.1)
    y_02 = taylor_series_method(0.1, y_01, 0.1)

    print("\nTask 7: Taylor Series Method")
    print(f"y(0.1) using Taylor Series: {y_01:.6f}")
    print(f"y(0.2) using Taylor Series: {y_02:.6f}")

import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


def random_search(func, bounds, num_iterations=1000):
    dim = len(bounds)
    best_x = None
    best_f = float('inf')
    history = []

    for _ in range(num_iterations):
        x = np.array([np.random.uniform(low, high) for (low, high) in bounds])
        f_val = func(x)
        history.append((x[0], x[1], f_val))

        if f_val < best_f:
            best_x = x
            best_f = f_val

    return best_x, best_f, history


def plot_optimization_process(history, best_x, best_f, bounds, func):
    x = np.linspace(bounds[0][0], bounds[0][1], 100)
    y = np.linspace(bounds[1][0], bounds[1][1], 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[func(np.array([x_, y_])) for x_, y_ in zip(x_row, y_row)] for x_row, y_row in zip(X, Y)])

    hx, hy, hz = zip(*history)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)
    ax.scatter(hx, hy, hz, c='red', s=10, label='Случайные точки', alpha=0.4)
    ax.scatter(best_x[0], best_x[1], best_f, color='black', s=50, label='Найденный минимум')

    ax.set_title("Метод случайного поиска в 3D")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.legend()

    plt.show()


if __name__ == "__main__":
    # Целевая функция задана через lambda (x^2 + y^2)
    func = lambda x: x[0] ** 2 + x[1] ** 2

    bounds = [(-5, 5), (-5, 5)]
    num_iterations = 10

    best_x, best_f, history = random_search(func, bounds, num_iterations)

    print(f"Лучшее решение: x = {best_x}")
    print(f"Значение функции: f(x) = {best_f}")

    print(tabulate(history, headers=['x1', 'x2', 'f']))
    plot_optimization_process(history, best_x, best_f, bounds, func)

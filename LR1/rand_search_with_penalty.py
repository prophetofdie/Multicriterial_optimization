import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# === Ограничения ===
constraints = [
    lambda x: x[0] + x[1] - 3,   # x + y <= 3 → x + y - 3 <= 0
    lambda x: -x[0],             # x >= 0 → -x <= 0
    lambda x: -x[1],             # y >= 0 → -y <= 0
]

# === Штрафная функция ===
def penalty(x, constraints):
    return sum(max(0, g(x))**2 for g in constraints)

# === Целевая функция с добавлением штрафа ===
def penalized_func(x, r=1000):
    original = x[0] ** 2 + x[1] ** 2
    penalty_term = penalty(x, constraints)
    return original + r * penalty_term

# === Метод случайного поиска ===
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

# === Визуализация ===
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

    ax.set_title("Метод штрафных функций (случайный поиск)")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('F(x)')
    ax.legend()

    plt.show()

# === Основной блок ===
if __name__ == "__main__":
    bounds = [(-1, 5), (-1, 5)]
    num_iterations = 10
    r = 1000  # коэффициент штраф

    best_x, best_f, history = random_search(lambda x: penalized_func(x, r), bounds, num_iterations)

    print(f"Лучшее решение: x = {best_x}")
    print(f"Значение исходной функции: f(x) = {best_x[0]**2 + best_x[1]**2}")
    print(f"Штраф: {penalty(best_x, constraints)}")

    plot_optimization_process(history, best_x, best_f, bounds, lambda x: penalized_func(x, r))

    print(tabulate(history, headers=['x1', 'x2', 'f']))

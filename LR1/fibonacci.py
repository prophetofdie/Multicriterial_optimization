from typing import Callable
from matplotlib import pyplot as plt


def fibonacci_search(func: Callable[[float], float], a: float, b: float, eps: float) -> float:
    """
    Метод Фибоначчи для одномерной оптимизации (нахождение минимума функции на отрезке [a, b]).

    :param func: Одномерная функция f(x), которую нужно минимизировать
    :param a: Левая граница интервала поиска
    :param b: Правая граница интервала поиска
    :param eps: Желаемая точность (максимально допустимая длина финального интервала)
    :return: Приближённое значение x, при котором f(x) минимально на [a, b]
    """

    # Построение последовательности Фибоначчи до тех пор, пока последний элемент не превысит (b - a) / eps
    F = [1, 1]
    while F[-1] < (b - a) / eps:
        F.append(F[-1] + F[-2])
    n = len(F) - 1  # Количество шагов (итераций), необходимое для достижения нужной точности

    print(f"Последовательность Фибоначчи до {n}-го элемента: {F}")

    # Вычисление начальных точек x1 и x2 внутри интервала [a, b]
    x1 = a + (F[n - 2] / F[n]) * (b - a)
    x2 = a + (F[n - 1] / F[n]) * (b - a)

    f1 = func(x1)
    f2 = func(x2)

    print(f"Итерация 0: a={a:.5f}, b={b:.5f}, x1={x1:.5f}, x2={x2:.5f}, f1={f1:.5f}, f2={f2:.5f}")

    # Цикл сужения интервала
    for k in range(1, n - 1):
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (F[n - k - 1] / F[n - k]) * (b - a)
            f2 = func(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (F[n - k - 2] / F[n - k]) * (b - a)
            f1 = func(x1)

        print(f"Итерация {k}: a={a:.5f}, b={b:.5f}, x1={x1:.5f}, x2={x2:.5f}, f1={f1:.5f}, f2={f2:.5f}")

    x_min = (x1 + x2) / 2
    print(f"Финальный интервал: [{x1:.5f}, {x2:.5f}]")
    print(f"Приближённый минимум x = {x_min:.5f}")
    return x_min


if __name__ == '__main__':
    f = lambda x: x ** 2 - 6 * x + 30
    a = -10
    b = +15
    eps = 0.01
    x_opt = fibonacci_search(f, a, b, eps)
    print(f"Минимум {f(x_opt)} найден в точке x = {x_opt}")
    function_graph = [f(i / 100) for i in range(a * 100, b * 100)]
    x_cords = [i / 100 for i in range(a * 100, b * 100)]
    plt.plot(x_cords, function_graph)
    plt.axvline(x=x_opt, color='red', linestyle='--', label=f'x ≈ {x_opt:.2f}')
    plt.title('График функции и найденный минимум')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

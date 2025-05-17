import pandas as pd

from wsm import WSM


def PC(normalized_df: pd.DataFrame, weights: list[list]) -> dict:
    """
    Описание: Взвешенная сумма на базе парных сравнений
              Шаги:
              Нормализуем критерии
              1. Построим матрицу парных сравнений (метод Аналитического иерархического процесса, AHP).
              2. Рассчитаем веса как нормализованные суммы по столбцам.
              3. Используем как в методе (a) — СУММПРОИЗВ.

    :param normalized_df: Нормализованные данные
    :param weights: Матрица парных сравнений
    :return: Словарь значений с итоговой оценкой
    """

    # Суммирование веса критерия по строке
    summ_weights = [0 for i in weights]
    for id_row in range(0, len(weights)):
        for id_column in range(0, len(weights)):
            summ_weights[id_row] += weights[id_row][id_column]

    # Нормализация весов
    for id_row in range(0, len(weights)):
        for id_column in range(0, len(weights)):
            weights[id_row][id_column] = weights[id_row][id_column] / summ_weights[id_row]

    # Среднее значение нормализованных весов
    final_weights = [0 for i in weights]
    for id_row in range(0, len(weights)):
        for id_column in range(0, len(weights)):
            # Суммирование веса критерия по столбцу
            final_weights[id_row] += weights[id_column][id_row]
        final_weights[id_row] /= len(final_weights)

    # Метод взвешенной суммы c средними значениями нормализованных весов
    return WSM(normalized_df, final_weights)
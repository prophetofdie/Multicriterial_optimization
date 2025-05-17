import math
import pandas as pd


def ideal_point(normalized_df: pd.DataFrame, ideal_poit: list, dir_norm: dict[str: bool], col_extr: list) -> dict:
    """
    Описание: Метод идеальной точки
              Шаги:
              1. Нормализуем критерии
              2. Определим идеальный (наилучший) вариант.
              3. Вычислим расстояние (евклидово) до идеальной точки.
              4. Чем ближе к идеальной — тем лучше.
    :param normalized_df: Нормализованные данные
    :param ideal_poit: Идеальный (наилучший) вариант
    :param dir_norm: Направление оптимизации параметров
    :param col_extr: Экстремумы исходных данных
    :return: Словарь значений с итоговой оценкой
    """
    def least_squares(point1: list, point2: list) -> float:
        """
        Описание: Метод наименьших квадратов: sqrt(Sum where i=[0, len(points)] ((point1_i-point2_i)^2)
                  Нахождение расстояния между двумя точками
        :param point1: Точка 1
        :param point2: Точка 2
        :return: Расстояние между точками
        """
        dist = 0.0
        for i in range(len(point1)):
            dist += math.pow(point1[i] - point2[i], 2)
        return math.sqrt(dist)

    data_columns = normalized_df.columns.to_list()  # Список наименований столбцов

    ideal_poit_norm = [
        ideal_poit[i-1] / col_extr[i-1] if dir_norm[data_columns[i]]
        else col_extr[i-1] / ideal_poit[i-1]
        for i in range(1, len(data_columns))
    ]  # Нормализация идеальной точки

    evaluation = dict()
    for string in range(0, len(normalized_df)):  # Сбор оценок для каждой строки данных
        df_string = normalized_df.iloc[string].to_list()
        element = ''.join(df_string[0])
        evaluation[element] = least_squares(ideal_poit_norm, df_string[1::])
    return evaluation

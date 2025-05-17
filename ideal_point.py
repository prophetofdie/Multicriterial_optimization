import math

import pandas as pd


def ideal_point(normalized_df: pd.DataFrame, ideal_poit: list, dir_norm: dict[str: bool], col_extr: list) -> dict:
    data_columns = normalized_df.columns.to_list()

    def least_squares(point1: list, point2: list) -> float:
        dist = 0.0
        for i in range(len(point1)):
            dist += math.pow(point1[i] - point2[i], 2)
        return math.sqrt(dist)

    ideal_poit_norm = [
        ideal_poit[i-1] / col_extr[i-1] if dir_norm[data_columns[i]]
        else col_extr[i-1] / ideal_poit[i-1]
        for i in range(1, len(data_columns))
    ]  # Нормализация идеальной точки

    evaluation = dict()
    for string in range(0, len(normalized_df)):
        df_string = normalized_df.iloc[string].to_list()
        element = ''.join(df_string[0])
        evaluation[element] = least_squares(ideal_poit_norm, df_string[1::])
    return evaluation

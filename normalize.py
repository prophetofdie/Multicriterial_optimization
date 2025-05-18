import pandas as pd
from tabulate import tabulate


def normalize_function(in_df: pd.DataFrame, dir_norm: dict[str: bool]) -> (pd.DataFrame, list):
    """
    Описание: Нормализация набора данных
    :param in_df: Входной набор данных
    :param dir_norm: Направление нормализации для столбцов исходных данных
    :return: Нормализованный набор данных
    """
    data_columns = in_df.columns.to_list()  # Список наименований столбцов

    col_extr = [
        max(in_df[data_columns[i]].to_list()) if dir_norm[data_columns[i]] else min(in_df[data_columns[i]].to_list())
        for i in range(1, len(data_columns))
    ]  # Поиск экстремумов для столбца в заданном направлении оптимизации

    normalized_df = pd.DataFrame(columns=data_columns)  # Создание заготовки для нормализованного набора данных
    for string in range(0, len(in_df)):
        in_df_string = in_df.iloc[string].to_list()
        key_column_name = ''.join(in_df_string[0])
        norm_df_string = list()
        for column in range(1, len(in_df_string)):
            norm_df_string.append(
                # Делим значение на максимум, если направление -- максимизация
                # Делим минимум на значение, если направление -- минимизация
                in_df_string[column]/col_extr[column-1] if dir_norm[data_columns[column]]
                else col_extr[column-1]/in_df_string[column]
            )
        # Добавление строки в нормализованный набор данных
        normalized_df.loc[string] = [key_column_name] + norm_df_string
    return normalized_df, col_extr


def print_rating(evaluation_dict: dict[str: int], direction=True) -> None:
    """
    Описание: Вывод ранжированных в заданном направлении
    :param evaluation_dict: Словарь полученных оценок
    :param direction: Направление ранжирования (True -- если оптимальным является значение с максимальной оценкой,
                                                False -- если оптимальным является значение с минимальной оценкой
    :return: -
    """
    # Сортировка словаря по значениям
    rating = sorted(evaluation_dict.items(), key=lambda item: item[1], reverse=direction)
    numbered_data = [(f'Место {i + 1}', *row) for i, row in enumerate(rating)]

    print(tabulate(numbered_data, headers=['№', 'Оружие', 'Рейтинг']))

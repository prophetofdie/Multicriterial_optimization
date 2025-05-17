import pandas as pd


def hermeyer_bundle(normalized_df: pd.DataFrame, weights: list) -> dict:
    """
    Описание: Выбираем альтернативу, у которой все критерии сбалансированы — нет "провала" по одному из важнейших
              критериев. То есть приоритет отдается тому, у кого наихудшее отношение (N/w) — лучше всех.
    :param normalized_df: Нормализованные данные
    :param weights: Веса
    :return: Словарь значений с итоговой оценкой
    """
    evaluation = dict()  # Словарь оценок
    for string in range(0, len(normalized_df)):
        df_string = normalized_df.iloc[string].to_list()
        element = ''.join(df_string[0])
        # Отношение не может быть больше единицы => всегда будем получать валидное значение при стартовом значении 1
        worst_element_evaluation = 1
        for id_column in range(1, len(df_string)):  # Находим минимальное отношение для строки
            worst_element_evaluation = min(df_string[id_column] / weights[id_column - 1], worst_element_evaluation)
        evaluation[element] = worst_element_evaluation
    return evaluation

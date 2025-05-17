import pandas as pd


def MC(normalized_df: pd.DataFrame, weights: list) -> dict:
    """
    Описание: Мультипликативная свёртка
              Шаги:
              1. Нормализуем критерии.
              2. Возведем каждую нормализованную оценку в степень веса.
              3. Перемножим: =ПРОИЗВ(нормализованные^вес)
    :param normalized_df: Нормализованные данные
    :param weights: Веса
    :return: Словарь значений с итоговой оценкой
    """
    evaluation = dict()
    for string in range(0, len(normalized_df)):  # Проход по строкам данных
        df_string = normalized_df.iloc[string].to_list()
        element = ''.join(df_string[0])
        element_evaluation = 1
        for id_column in range(1, len(df_string)):  # Нахождение общей оценки для строки
            element_evaluation *= df_string[id_column] ** weights[id_column-1]
        evaluation[element] = element_evaluation
    return evaluation

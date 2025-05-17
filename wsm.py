import pandas as pd


def WSM(normalized_df: pd.DataFrame, weights: list) -> dict:
    """
    Описание: Метод взвешенной суммы
              Шаги:
              1. Нормализуем критерии
              2. Введем веса критериев в отдельный диапазон.
              3. Итоговая оценка = СУММПРОИЗВ(нормализованные значения; веса)
    :param normalized_df: Нормализованные данные
    :param weights: Веса
    :return: Словарь значений с итоговой оценкой
    """
    evaluation = dict()
    for string in range(0, len(normalized_df)):  # Проход по всем строкам набора данных
        df_string = normalized_df.iloc[string].to_list()
        element = ''.join(df_string[0])
        element_evaluation = 0
        for id_column in range(1, len(df_string)):
            # Суммирование оценки по строке
            element_evaluation += df_string[id_column] * weights[id_column-1]
        evaluation[element] = element_evaluation
    return evaluation

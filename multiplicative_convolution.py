import pandas as pd

from normalize import data_columns, normalize_function, print_rating


def WSM(normalized_df: pd.DataFrame, weights: list) -> dict:
    evaluation = dict()
    for string in range(0, len(normalized_df)):
        df_string = normalized_df.iloc[string].to_list()
        element = ''.join(df_string[0])
        element_evaluation = 0
        for id_column in range(1, len(df_string)):
            element_evaluation *= df_string[id_column] * weights[id_column-1]
        evaluation[element] = element_evaluation
    return evaluation
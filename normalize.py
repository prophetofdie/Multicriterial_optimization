import pandas as pd

data_columns = ['МАШИНА', 'цена (Р)', 'год выпуска', 'пробег (км)', 'налог (Р/Год)',
                'объем двигателя (литров)', 'кол-во л.с.', 'тип коробки передач']


def normalize_function(in_df: pd.DataFrame, dir_norm: dict[str: bool]) -> pd.DataFrame:
    col_extr = [
        max(in_df[data_columns[i]].to_list()) if dir_norm[data_columns[i]] else min(in_df[data_columns[i]].to_list())
        for i in range(1, len(data_columns))
    ]  # Поиск экстремумов для столбца в заданном направлении оптимизации

    normalized_df = pd.DataFrame(columns=data_columns)
    for string in range(0, len(in_df)):
        in_df_string = in_df.iloc[string].to_list()
        key_column_name = ''.join(in_df_string[0])
        norm_df_string = list()
        for column in range(1, len(in_df_string)):
            norm_df_string.append(
                in_df_string[column]/col_extr[column-1] if dir_norm[data_columns[column]]
                else col_extr[column-1]/in_df_string[column]
            )
        normalized_df.loc[string] = [key_column_name] + norm_df_string
    return normalized_df


def print_rating(evaluation_dict: dict[str: int], direction=True) -> None:
    rating = sorted(evaluation_dict.items(), key=lambda item: item[1], reverse=True)
    chosen_range = range(0, len(rating)) if direction else range(len(rating)-1, -1, -1)
    for i in chosen_range:

        print(f"{rating[i]}: МЕСТО {i+1}")


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


def WSM(normalized_df: pd.DataFrame, weights: list) -> dict:
    evaluation = dict()
    for string in range(0, len(normalized_df)):
        df_string = normalized_df.iloc[string].to_list()
        element = ''.join(df_string[0])
        element_evaluation = 0
        for id_column in range(1, len(df_string)):
            element_evaluation += df_string[id_column] * weights[id_column-1]
        evaluation[element] = element_evaluation
    return evaluation


if __name__ == "__main__":
    input_data = pd.DataFrame(
        [['Honda Integra III', 500000, 1998, 190000, 4080, 1.6, 120, 1],
         ['Mitsubishi Eclipse III', 625000, 2003, 172500, 4896, 2.4, 149, 2],
         ['Nissan Skyline X', 790000, 1999, 360000, 9751, 2.5, 200, 2],
         ['BMW 5 серии 520i', 900000, 1988, 300000, 4386, 2.0, 129, 1],
         ['Lexus GS 400', 600000, 1998, 600000, 44100, 4.0, 294, 2],
         ['Nissan Laurel', 615000, 1998, 400000, 4760, 2.0, 155, 2],
         ['Mazda RX-8', 800000, 2003, 109000, 9653, 1.3, 192, 2],
         ['Mercedes-Benz CLC-Класс 230', 955000, 2008, 154000, 14688, 2.5, 204, 2],
         ['Honda Civic', 1000000, 1995, 220000, 2828, 1.5, 101, 1],
         ['Toyota Carina ED', 270000, 1993, 502983, 1300, 2.0, 140, 2]],
        columns=data_columns
    )

    # True - максимизация, False - минимизация
    direction_optimisation = {
        data_columns[1]: False,
        data_columns[2]: True,
        data_columns[3]: False,
        data_columns[4]: False,
        data_columns[5]: True,
        data_columns[6]: True,
        data_columns[7]: True,
    }

    norm_df = normalize_function(input_data, direction_optimisation)
    print_rating(WSM(norm_df, [0.8, 0.2, 1.0, 0.7, 0.6, 0.6, 0.4]), False)
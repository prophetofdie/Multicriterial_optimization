import pandas as pd

from ideal_point import ideal_point
from multiplicative_convolution import MC
from hermeyer_bundle import hermeyer_bundle
from normalize import normalize_function, print_rating
from pairwise_comparisons import PC
from wsm import WSM


if __name__ == "__main__":
    #  Исходные данные
    data_columns = ['Оружие', 'Стоимость ($)', 'Емкость магазина (шт)',
                'Скорострельность (выстр./мин)', 'Время перезарядки (С)',
                'Скорость передвижения (u/c)', 'Урон', 'Дальность поражения (m)']

    input_data = pd.DataFrame(
        [['АК-47', 2700, 30, 600, 2.5, 215, 36, 24],
        ['M4A1-S', 2900, 20, 600, 3.1, 225, 38, 30],
        ['M4A1', 3000, 30, 666, 3.1, 225, 33, 30],
        ['AUG', 3300, 30, 600, 3.8, 220, 28, 31],
        ['FAMAS', 1950, 25, 800, 3, 220.0, 30, 21],
        ['GALIL', 1800, 35, 666, 3, 215.0, 30, 18],
        ['SG553', 3000, 30, 543, 2.8, 210, 30, 26],
        ['MP9', 1250, 30, 857, 2.1, 240, 26, 17],
        ['AWP', 4750, 5, 41, 3.6, 100.0, 115, 76],
        ['SSG08', 1700, 10, 48, 3.7, 230.0, 88, 52]],
        columns=data_columns
    )

    # Направление оптимизации: True - максимизация, False - минимизация
    direction_optimisation = {
        data_columns[1]: False,
        data_columns[2]: True,
        data_columns[3]: True,
        data_columns[4]: False,
        data_columns[5]: True,
        data_columns[6]: True,
        data_columns[7]: True,
    }

    norm_df, extramural = normalize_function(input_data, direction_optimisation)
    print(norm_df)

    print("МЕТОД ВЗВЕШЕННОЙ СУММЫ")
    weights_wsm = [0.7, 0.3, 0.4, 0.1, 0.6, 1, 0.8]  # Веса метода взвешенной суммы
    print_rating(WSM(norm_df, weights_wsm), True)
    print("\nВзвешенная сумма на базе парных сравнений")
    weights_pc = [
        [1.00, 0.10, 0.30, 0.60, 1.50, 1.80, 0.60],
        [10.00, 1.00, 0.50, 0.40, 1.75, 3.00, 0.50],
        [3.33, 2.00, 1.00, 0.20, 1.50, 1.20, 0.50],
        [1.67, 2.50, 5.00, 1.00, 1.20, 1.40, 0.30],
        [0.67, 0.57, 0.67, 0.83, 1.00, 1.30, 0.20],
        [0.56, 0.33, 0.83, 0.71, 0.77, 1.00, 0.10],
        [1.67, 2.00, 2.00, 3.33, 5.00, 10.00, 1.00]
    ]
    print_rating(PC(norm_df, weights_pc), True)
    print("\nМЕТОД МУЛЬТИПЛИКАТИВНОЙ СВЕРТКИ")
    weights_mc = weights_wsm  # Веса метода мультипликативной свертки
    print_rating(MC(norm_df, weights_mc), True)
    print("\nМЕТОД ИДЕАЛЬНЫХ ТОЧЕК")
    ideal_point_str = [2700, 30, 600, 2.5, 215, 36, 24]  # Идеальная точка
    print_rating(ideal_point(norm_df, ideal_point_str, direction_optimisation, extramural), False)
    print("\nМетод Гермейера")
    weights_bundle = weights_wsm  # Веса свертки Гермейера
    print_rating(hermeyer_bundle(norm_df, weights_bundle), True)

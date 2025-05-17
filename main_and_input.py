import pandas as pd

from ideal_point import ideal_point
from multiplicative_convolution import MC
from normalize import normalize_function, print_rating
from wsm import WSM

data_columns = ['МАШИНА', 'цена (Р)', 'год выпуска', 'пробег (км)', 'налог (Р/Год)',
                'объем двигателя (литров)', 'кол-во л.с.', 'тип коробки передач']

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

    norm_df, extramural = normalize_function(input_data, direction_optimisation)
    print("МЕТОД ВЗВЕШЕННОЙ СУММЫ")
    weights_wsm = [0.8, 0.2, 1.0, 0.7, 0.6, 0.6, 0.4]  # Веса метода взвешенной суммы
    print_rating(WSM(norm_df, weights_wsm), True)
    print("\nМЕТОД МУЛЬТИПЛИКАТИВНОЙ СВЕРТКИ")
    weights_mc = [0.8, 0.2, 1.0, 0.7, 0.6, 0.6, 0.4]  # Веса метода мультипликативной свертки
    print_rating(MC(norm_df, weights_mc), True)
    print("\nМЕТОД ИДЕАЛЬНЫХ ТОЧЕК")
    ideal_point_str = [1500000, 1989, 70200, 3000, 1.6, 115, 1]  # Идеальная точка
    print_rating(ideal_point(norm_df, ideal_point_str, direction_optimisation, extramural), False)


from pandas import DataFrame


def calculate_and_display_average_price(data: DataFrame):
    """
        Вычисляет и выводит среднюю цену закрытия акций за заданный период.

    :param data:
        Принимает DataFrame и вычисляет среднее значение колонки 'Close'.
    :return:
        Результат выводится в консоль.
    """
    print(f"Средняя цена закрытия акций за заданный период: {data['Close'].mean():.3f}")

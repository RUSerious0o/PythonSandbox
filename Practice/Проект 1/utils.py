from pandas import DataFrame
import csv


def calculate_and_display_average_price(data: DataFrame):
    """
        Вычисляет и выводит среднюю цену закрытия акций за заданный период.
        Принимает DataFrame и вычисляет среднее значение колонки 'Close'.
        Результат выводится в консоль.

    :param data: pandes.DataFrame, данные об акциях за период
    :return: None
    """

    print(f"Средняя цена закрытия акций за заданный период: {data['Close'].mean():.3f}")


def notify_if_strong_fluctuations(data: DataFrame, threshold: float):
    """
        Анализирует данные и уведомляет пользователя, если цена акций колебалась более чем на заданный процент за период.
        Функция вычисляет максимальное и минимальное значения цены закрытия и сравнивает разницу с заданным порогом.
        Если разница превышает порог, пользователь получает уведомление.

    :param data: pandes.DataFrame, данные об акциях за период
    :param threshold: float,    порог разницы между максимальным и минимальным значение закрытия цены акций
                                в заданном периоде, в процентах
    :return: None
    """

    diff = (data['Close'].max() - data['Close'].min()) / data['Close'].max()
    if diff >= threshold / 100:
        print(f'В заданном периоде цена акций колебалась более, чем на заданный процент ({threshold:.2f} %)')


def export_data_to_csv(data: DataFrame, filename: str):
    """
        Функция сохраняет загруженные данные об акциях в CSV файл.
        Функция принимает DataFrame и имя файла, после чего сохраняет данные в указанный файл.

    :param data: pandas.DataFrame, данные об акциях за период
    :param filename:
    :return: None
    """

    data.to_csv(filename, encoding='utf-8')

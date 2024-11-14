import os
import json
import csv
from pprint import pprint


class PriceMachine():
    DATA_PATH = './data'

    _COLUMNS = [
        ['товар', 'название', 'наименование', 'продукт'],
        ['розница', 'цена'],
        ['вес', 'масса', 'фасовка'],
    ]
    
    def __init__(self):
        self.data = []
        self.result = ''
        self.name_length = 0

    def load_prices(self, file_path=''):
        '''
            Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт
                
            Допустимые названия для столбца с ценой:
                розница
                цена
                
            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка
        '''

        files = os.listdir(file_path)
        for file in files:
            if 'price' in file:
                with open(os.path.join(file_path, file), 'r', encoding='utf-8') as data:
                    reader = csv.reader(data)
                    headers = next(reader)
                    print(headers)
                    columns = PriceMachine._search_product_price_weight(self, headers)
                    print(columns)
                    for row in reader:
                        data = []
                        for column in columns:
                            data.append(row[column])
                        data.append(file)
                        data.append(float(data[1]) / float(data[2]))
                        self.data.append(data)

        # pprint(self.data)
        self.data.sort(key=lambda x: int(x[4]), reverse=False)
        # pprint(self.data)


    def _search_product_price_weight(self, headers):
        '''
            Возвращает номера столбцов
        '''

        col_nums = []
        for col_values in PriceMachine._COLUMNS:
            for value in col_values:
                for i in range(len(headers)):
                    if value == headers[i]:
                        col_nums.append(i)

        return col_nums


    def export_to_html(self, fname='output.html'):
        result = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Позиции продуктов</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>Номер</th>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Фасовка</th>
                    <th>Файл</th>
                    <th>Цена за кг.</th>
                </tr>
        '''
    
    def find_text(self, text):
        print(f'{"№":4}'
              f'{"Наименование":60}'
              f'{"цена":8}'
              f'{"вес":8}'
              f'{"файл":16}'
              f'{"цена за кг"}')

        counter = 0
        for row in self.data:
            if text.lower() in str(row[0]).lower():
                counter += 1
                print(f'{str(counter):4}'
                      f'{row[0]:60}'
                      f'{row[1]:8}'
                      f'{row[2]:8}'
                      f'{row[3]:16}'
                      f'{row[4]:.1f}')

    
pm = PriceMachine()
print(pm.load_prices(PriceMachine.DATA_PATH))

'''
    Логика работы программы
'''

pm.find_text('щук')

print('the end')
print(pm.export_to_html())

import os
import json
import csv


class PriceMachine:
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

        file_names = os.listdir(file_path)
        for file_name in file_names:
            if 'csv' not in file_name:
                continue

            if 'price' in file_name:
                with open(os.path.join(file_path, file_name), 'r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    headers = next(reader)
                    columns = PriceMachine._search_product_price_weight(self, headers)
                    for row in reader:
                        data = []
                        for column in columns:
                            data.append(row[column])
                        data.append(file_name)
                        data.append(float(data[1]) / float(data[2]))
                        self.data.append(data)

        self.data.sort(key=lambda x: int(x[4]), reverse=False)
        return 'Данные успешно загружены!\n'


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
                        break

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

        for item_num, item in enumerate(self.data, start=1):
            name, price, weight, file, price_per_weight = item
            result += '<tr>'
            result += f'<td>{item_num}</td>'
            result += f'<td>{name}</td>'
            result += f'<td>{price}</td>'
            result += f'<td>{weight}</td>'
            result += f'<td>{file}</td>'
            result += f'<td>{price_per_weight:.2f}</td>'

        result += '</table></body>'

        with open(fname, 'w', encoding='utf-8') as file:
            file.write(result)

        return 'Данные успешно выгружены!'
    
    def find_text(self, text):
        result = []
        for row in self.data:
            if text.lower() in str(row[0]).lower():
                result.append(row)

        return result

    
pm = PriceMachine()
print(pm.load_prices(PriceMachine.DATA_PATH))

'''
    Логика работы программы
'''

upload_request = input('Желаете сохранить данные в формете html? (д/н) ')
if upload_request.lower() == 'д':
    print(pm.export_to_html())

while(True):
    text = input('Введите данные для поиска (exit для выхода): ')
    if text.lower() == 'exit':
        break

    print('\nНайденные позиции:')
    print(f'{"№":4}'
          f'{"Наименование":60}'
          f'{"цена":8}'
          f'{"вес":8}'
          f'{"файл":16}'
          f'{"цена за кг"}')

    counter = 0
    data = pm.find_text(text)
    for row in data:
        counter += 1
        print(f'{str(counter):4}'
              f'{row[0]:60}'
              f'{row[1]:8}'
              f'{row[2]:8}'
              f'{row[3]:16}'
              f'{row[4]:.2f}')

print('the end')

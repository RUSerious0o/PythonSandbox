from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Confirm, IntPrompt
from rich.columns import Columns

m_console = Console(width=600)
info_panel = Panel(title='Тестовая панель', width=40, renderable="Выберите операцию:\n" +\
                   "1. Добавить товар\n" +\
                   "2. Очистить корзину\n" +\
                   "3. Создать чек\n" +\
                   "4. Выйти")

def get_cart_panel(cart, cart_panel_width = 100, panel_name = 'Корзина'):
    def get_column_names(item_):
        names = []
        for key in dict(item_).keys():
            names.append(key)

        return names

    result_panel = Panel(title=panel_name, width=cart_panel_width, renderable='')

    if len(cart) == 0:
        return result_panel

    column_names = get_column_names(cart[0])
    cart_columns_dict = {}
    for columns_name in column_names:
        cart_columns_dict[columns_name] = []

    for item in cart:
        for key, value in item.items():
            cart_columns_dict[key].append(value)

    cart_columns = Columns([])
    column_width = cart_panel_width // len(cart_columns_dict) - 2
    for key, items in cart_columns_dict.items():
        cart_columns.add_renderable(Panel(title=key, width=column_width, renderable='\n'.join(map(str, items))))

    result_panel.renderable = cart_columns
    return result_panel


def get_cost(cart, key):
    cost = [0]
    for item in list(cart):
        cost.append(dict(item)[key])

    return round(sum(cost), 2)


def run(add_test_cart=True):
    cart = []
    NAME_KEY = 'Название'
    VOLUME_KEY = 'Количество'
    PRICE_KEY = 'Цена'
    COST_KEY = 'Сумма'
    keys_list = [NAME_KEY, VOLUME_KEY, PRICE_KEY, COST_KEY]

    if(add_test_cart):
        cart.append({NAME_KEY: 'Milk', VOLUME_KEY: 1, PRICE_KEY: 100, COST_KEY: 200})
        cart.append({NAME_KEY: 'Sugar', VOLUME_KEY: 2, PRICE_KEY: 10, COST_KEY: 20})
        cart.append({NAME_KEY: 'Banananananananananananas', VOLUME_KEY: 3, PRICE_KEY: 15.3, COST_KEY: 45.9})

    while(True):
        m_console.print(Columns([info_panel, get_cart_panel(cart)]))
        option = m_console.input('Выберите действие: ')[0]

        if option == '4':
            break
        elif option == '1':
            name = m_console.input('Введите название: ')
            volume = m_console.input('Введите количество: ')
            price = m_console.input('Введите цену: ')
            if(not (volume.replace('.', '').isnumeric() and
                    price.replace('.', '').isnumeric())):
                m_console.print('Неверный ввод')
                continue

            cart.append({NAME_KEY: name, VOLUME_KEY: volume, PRICE_KEY: price, COST_KEY: round(float(volume) * float(price), 2)})
        elif option == '2':
            cart.clear()
        elif option == '3':
            text =  '\tСпасибо за покупку\n' + \
                    '\t__________________\n' + \
                    f'\tКоличество товаров:\t{len(cart)}\n' +\
                    f'\tОбщая стоимость:\t{get_cost(cart, COST_KEY)}\n' +\
                    '\tПокупатель: Хороший Человек\n' +\
                    '\tАдрес магазина: Спб, Невский пр., д. 1'

            m_console.print(Panel(title='Чек', width=60, renderable=text))
            break

        else:
            m_console.print('Выбрано неизвестное действие!')
            continue


run()

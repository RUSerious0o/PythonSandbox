import sqlite3


class ProductsTable:
    name = 'Products'

    class Columns:
        id = 'id'
        title = 'title'
        description = 'description'
        price = 'price'
        picture_path = 'picture_path'


def initiate_db():
    with sqlite3.connect('not_telegram.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'DROP TABLE IF EXISTS {ProductsTable.name}')
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {ProductsTable.name} ('
                       f'{ProductsTable.Columns.id} INTEGER PRIMARY KEY, '
                       f'{ProductsTable.Columns.title} TEXT NOT NULL, '
                       f'{ProductsTable.Columns.description} TEXT, '
                       f'{ProductsTable.Columns.price} INTEGER NOT NULL, '
                       f'{ProductsTable.Columns.picture_path} TEXT'
                       f')')
        connection.commit()

        if cursor.execute(f"SELECT COUNT({ProductsTable.Columns.id}) FROM {ProductsTable.name}").fetchone()[0] == 0:
            fill_initial_data()


def fill_initial_data():
    data = [
        ('\"Ананас консервированный\"', '\"Вы не поверите...\"', 200, '\"./pics/pineapple.png\"'),
        ('\"Молоко 2,5%\"', '\"Кто сказал, что это вредно?\"', 100, '\"./pics/milk.png\"'),
        ('\"Тыковка\"', '\"Просто тыковка\"', 400, '\"./pics/pump.png\"'),
        ('\"Куриная грудка, филе\"', '\"Куда же без нее?\"', 300, '\"./pics/chicken.png\"'),
    ]

    with sqlite3.connect('not_telegram.db') as connection:
        cursor = connection.cursor()
        for item in data:
            cursor.execute(f'INSERT INTO {ProductsTable.name} ('
                           f'{ProductsTable.Columns.title}, '
                           f'{ProductsTable.Columns.description}, '
                           f'{ProductsTable.Columns.price}, '
                           f'{ProductsTable.Columns.picture_path}'
                           f') VALUES ('
                           f'{item[0]}, '
                           f'{item[1]}, '
                           f'{item[2]}, '
                           f'{item[3]}'
                           f')')
        connection.commit()


def get_all_products():
    with sqlite3.connect('not_telegram.db') as connection:
        cursor = connection.cursor()
        result = cursor.execute(f'SELECT * FROM {ProductsTable.name}')
        return result.fetchall()


if __name__ == '__main__':
    initiate_db()

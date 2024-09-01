import sqlite3


class ProductsTable:
    name = 'Products'

    class Columns:
        id = 'id'
        title = 'title'
        description = 'description'
        price = 'price'
        picture_path = 'picture_path'


class BotUsersTable:
    name = 'Bot_users'
    start_balance = 1000

    class Columns:
        id = 'id'
        username = 'username'
        email = 'email'
        age = 'age'
        balance = 'balance'


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

        cursor.execute(f"DROP TABLE IF EXISTS {BotUsersTable.name}")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {BotUsersTable.name} ("
                       f"{BotUsersTable.Columns.id} INTEGER PRIMARY KEY,"
                       f"{BotUsersTable.Columns.username} TEXT UNIQUE NOT NULL,"
                       f"{BotUsersTable.Columns.email} TEXT UNIQUE NOT NULL,"
                       f"{BotUsersTable.Columns.age} INTEGER,"
                       f"{BotUsersTable.Columns.balance} INTEGER NOT NULL"
                       f")")


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


def add_user(username: str, email: str, age: int):
    with sqlite3.connect('not_telegram.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO {BotUsersTable.name} ('
                       f'{BotUsersTable.Columns.username}, '
                       f'{BotUsersTable.Columns.email}, '
                       f'{BotUsersTable.Columns.age}, '
                       f'{BotUsersTable.Columns.balance}'
                       f') VALUES ('
                       f'{"\"" + username + "\""}, '
                       f'{"\"" + email + "\""}, '
                       f'{age}, '
                       f'{BotUsersTable.start_balance}'
                       f')')
        connection.commit()


def is_included(username: str):
    with sqlite3.connect('not_telegram.db') as connection:
        cursor = connection.cursor()
        result = cursor.execute(f'SELECT COUNT({BotUsersTable.Columns.id}) '
                                f'FROM {BotUsersTable.name} '
                                f'WHERE {BotUsersTable.Columns.username} = {"\"" + username + "\""}')
        if result.fetchone()[0] == 0:
            return False
        else:
            return True


def delete_user(username: str):
    with sqlite3.connect('not_telegram.db') as connection:
        cursor = connection.cursor()
        result = cursor.execute(f'DELETE FROM {BotUsersTable.name} '
                                f'WHERE {BotUsersTable.Columns.username} = {"\"" + username + "\""}')


if __name__ == '__main__':
    initiate_db()

    add_user('me', '$$$', 30)
    print(is_included('me'), is_included('mee'))
    delete_user('me')
    print(is_included('me'))

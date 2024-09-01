import sqlite3
from pprint import pprint
from random import randint


class UserTable:
    name = 'Users'
    test_users_count = 100

    class Columns:
        id = 'id'
        username = 'username'
        email = 'email'
        age = 'age'
        balance = 'balance'


if __name__ == '__main__':
    with sqlite3.connect('not_telegram.db') as connection:

        cursor = connection.cursor()

        cursor.execute(f"DROP TABLE IF EXISTS {UserTable.name}")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {UserTable.name} ("
                       f"{UserTable.Columns.id} INTEGER PRIMARY KEY,"
                       f"{UserTable.Columns.username} TEXT UNIQUE NOT NULL,"
                       f"{UserTable.Columns.email} TEXT UNIQUE NOT NULL,"
                       f"{UserTable.Columns.age} INTEGER,"
                       f"{UserTable.Columns.balance} INTEGER NOT NULL"
                       f")")

        for i in range(1, UserTable.test_users_count + 1):
            cursor.execute(f"INSERT INTO {UserTable.name} ("
                           f"{UserTable.Columns.username},"
                           f"{UserTable.Columns.email},"
                           f"{UserTable.Columns.age},"
                           f"{UserTable.Columns.balance}"                       
                           f") VALUES ("
                           f"{'\"User' + str(i) + '\"'}, "
                           f"{'\"example' + str(i) + '@gmail.com\"'}, "
                           f"{randint(14, 70)}, "
                           f"{1000}"
                           f")")
        connection.commit()

        for i in range(1, UserTable.test_users_count + 1, 2):
            cursor.execute(f"UPDATE {UserTable.name} "
                           f"SET {UserTable.Columns.balance} = 500 "
                           f"WHERE {UserTable.Columns.id} = {i}")
        connection.commit()

        for i in range(1, UserTable.test_users_count + 1, 3):
            cursor.execute(f"DELETE FROM {UserTable.name} "
                           f"WHERE {UserTable.Columns.id} = {i}")
        connection.commit()

        sample_ = cursor.execute(f"SELECT "
                                 f"{UserTable.Columns.username}, "
                                 f"{UserTable.Columns.email}, "
                                 f"{UserTable.Columns.age}, "
                                 f"{UserTable.Columns.balance} "                          
                                 f"FROM  {UserTable.name} "
                                 f"WHERE {UserTable.Columns.age} >= {60}")
        pprint(sample_.fetchall())

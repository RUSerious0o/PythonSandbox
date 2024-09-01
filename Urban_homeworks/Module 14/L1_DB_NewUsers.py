import sqlite3
from pprint import pprint
from random import randint

with sqlite3.connect('not_telegram.db') as connection:

    cursor = connection.cursor()

    __USERS_TABLE_NAME = 'Users'
    __USERS_TABLE_COLUMNS = [
        'id',
        'username',
        'email',
        'age',
        'balance',
    ]
    __TEST_USERS_COUNT = 100

    cursor.execute(f"DROP TABLE IF EXISTS {__USERS_TABLE_NAME}")
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {__USERS_TABLE_NAME} ("
                   f"{__USERS_TABLE_COLUMNS[0]} INTEGER PRIMARY KEY,"
                   f"{__USERS_TABLE_COLUMNS[1]} TEXT UNIQUE NOT NULL,"
                   f"{__USERS_TABLE_COLUMNS[2]} TEXT UNIQUE NOT NULL,"
                   f"{__USERS_TABLE_COLUMNS[3]} INTEGER,"
                   f"{__USERS_TABLE_COLUMNS[4]} INTEGER NOT NULL"
                   f")")

    for i in range(1, __TEST_USERS_COUNT + 1):
        cursor.execute(f"INSERT INTO {__USERS_TABLE_NAME} ("
                       f"{__USERS_TABLE_COLUMNS[1]},"
                       f"{__USERS_TABLE_COLUMNS[2]},"
                       f"{__USERS_TABLE_COLUMNS[3]},"
                       f"{__USERS_TABLE_COLUMNS[4]}"
                       f") VALUES ("
                       f"{'\"User' + str(i) + '\"'}, "
                       f"{'\"example' + str(i) + '@gmail.com\"'}, "
                       f"{randint(14, 70)}, "
                       f"{1000}"
                       f")")
    connection.commit()

    for i in range(1,  __TEST_USERS_COUNT + 1, 2):
        cursor.execute(f"UPDATE {__USERS_TABLE_NAME} "
                       f"SET {__USERS_TABLE_COLUMNS[4]} = 500 "
                       f"WHERE {__USERS_TABLE_COLUMNS[0]} = {i}")
    connection.commit()

    for i in range(1,  __TEST_USERS_COUNT + 1, 3):
        cursor.execute(f"DELETE FROM {__USERS_TABLE_NAME} "
                       f"WHERE {__USERS_TABLE_COLUMNS[0]} = {i}")
    connection.commit()

    sample_ = cursor.execute(f"SELECT "
                             f"{__USERS_TABLE_COLUMNS[1]}, "
                             f"{__USERS_TABLE_COLUMNS[2]}, "
                             f"{__USERS_TABLE_COLUMNS[3]}, "
                             f"{__USERS_TABLE_COLUMNS[4]} "                         
                             f"FROM  {__USERS_TABLE_NAME} "
                             f"WHERE {__USERS_TABLE_COLUMNS[3]} >= {60}")
    pprint(sample_.fetchall())

import sqlite3
from L1_DB_NewUsers import UserTable

with sqlite3.connect('not_telegram.db') as connection:
    cursor = connection.cursor()

    cursor.execute(f"DELETE FROM {UserTable.name} "
                   f"WHERE {UserTable.Columns.id} = 6")
    connection.commit()

    result = cursor.execute(f"SELECT SUM({UserTable.Columns.balance}), "
                          f"AVG({UserTable.Columns.balance}), "
                          f"COUNT({UserTable.Columns.id}) "
                          f"FROM {UserTable.name}").fetchone()
    print(f'Всего пользователей: {result[2]},\n'
          f'Сумма всех балансов: {result[0]}\n'
          f'Средний баланс пользователей: {round(result[1], 2)}')

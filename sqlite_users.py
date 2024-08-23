import sqlite3

connection = sqlite3.connect('users-sqlite.db')

cursor = connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS Users 
    (user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL, active BOOLEAN NOT NULL)
''')

# usersToInsert = [
#     ('Adams Smith', 'Test', 1),
#     ('Bob Rick', 'Test', 1),
#     ('Cath Smith', 'Test', 1),
#     ('Davion Rock', 'Test', 1),
#     ('Emma Williams', 'Test', 1),
#     ('Ford Kim', 'Test', 1),
#     ('Garth Roth', 'Test', 0)
# ]



# cursor.executemany(''' 
#     INSERT INTO Users(username, password, active) VALUES(?,?,?)
#  ''', usersToInsert)

# get_active_users='1'
# cursor.execute("SELECT * FROM Users WHERE active=?", get_active_users)


# get_inactive_users='0'
# cursor.execute("SELECT * FROM Users WHERE active=?", get_inactive_users)


# active_user = '1'
# cursor.execute("UPDATE Users SET active = ? WHERE user_id = ?", [active_user, 7])

# delete_id = '2'
# cursor.execute("DELETE FROM Users WHERE user_id = ?", delete_id)


cursor.execute("SELECT * FROM Users")
print(cursor.fetchall())

print(cursor.fetchall())

connection.commit()
connection.close()


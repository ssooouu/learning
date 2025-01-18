import sqlite3


connection =  sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(10):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{i+1}', f'example{i+1}@gmail.com', f'{(1+i)*10}', f'{1000}'))


# cursor.execute('DELETE FROM Users WHERE balance = ?', (f'{1000}',))
# cursor.execute('DELETE FROM Users WHERE balance = ?', (f'{500}',))

for i in range(1, 11):
    if i %2 == 0:
        cursor.execute('UPDATE Users SET balance  = ? WHERE id = ?', (500, f'{i+1}'))
c = 3
for i in range(1,11):
    if c == 3:
        cursor.execute('DELETE FROM Users WHERE id = ?', (f'{i}',))
        c = 1
    else:
        c += 1

cursor.execute(' SELECT username, email, age, balance FROM Users WHERE age != ?', (f'{60}', ))

users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()



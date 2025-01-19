import sqlite3

connection = sqlite3.connect('telegram.db')
cursor = connection.cursor()





def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL)''')
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_title ON Products (title)")

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")



def add_user(username, email, age):
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))

    if check_user.fetchone() is None:
        cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'{username}', f'{email}', f'{age}', f'{1000}'))
        connection.commit()



def is_included(username):
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))

    if check_user.fetchone() is None:
        return False
    else:
        return True




def get_all_products():
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()
    a = []
    for product in products:
        a.append(product)
    return a


connection.commit()
# connection.close()

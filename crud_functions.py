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




# for i in range(1,5):
#     cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                    (f'title{i}', f'description{i}', f'price{i}'))



def get_all_products():
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()
    a = []
    for product in products:
        a.append(product)
    return a


connection.commit()
# connection.close()

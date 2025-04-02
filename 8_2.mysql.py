# import csv
# import pymysql

# config = {
#     'user':'root',
#     'password':'0000',
#     'host':'localhost',
#     'database':'my_db'
# }

# conn = pymysql.connect(**config)

# cursor = conn.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS books (
#         title VARCHAR(255),
#         author VARCHAR(255),
#         price DECIMAL(10, 2)
# """)

# with open('book_list.csv', mode='r', encoding='utf-8'):
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     for row in csv_reader:
#         title, author, price = row
#         price = float(price.replace('원', '').replace(',',''))
#         cursor.execute('''
#             INSERT INTO books (title, author, genre)
#         ''')
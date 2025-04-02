# import requests
# from bs4 import BeautifulSoup

# class Book:
#     def __init__(self, rank, title, author, price):
#         self.rank = rank
#         self.title = title
#         self.author = author
#         self.price = price

#     def __str__(self):
#         return f"{self.rank}위 : {self.title} - {self.author} - {self.price}"
    
#     def to_dict(self):
#         return {
#             'rank' : self.rank,
#             'title' : self.title,
#             'author' : self.author,
#             'price' : self.price
#         }

#     def to_list(self):
#         return [self.rank, self.title, self.author, self.price]

# url = 'https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# titles = [title.get_text(strip=True) for title in soup.select('div.info_row.info_name > a.gd_name')]
# authors = [author.get_text(strip=True) for author in soup.select('span.authPub.info_auth > a')]
# prices = [price.get_text(strip=True) for price in soup.select('div.info_row.info_price > strong > em')]
# ranks = [f"{i + 1}" for i in range(len(titles))]

# # Book 객체 생성
# books = []
# for i in range(len(titles)):
#     rank = i + 1
#     title = titles[i]
#     author = authors[i]
#     price = prices[i]
#     book = Book(rank, title, author, price)  # Book 객체 생성
#     books.append(book)

# # 책 정보 출력
# for book in books:
#     print(book)

# sqlite
# import sqlite3

# conn = sqlite3.connect('book.db')

# cursor = conn.cursor()
# cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS books(
#         rank INTEGER,
#         title TEXT,
#         author TEXT,
#         price TEXT
#         )
#     '''
# )

# for book in books:
#     cursor.execute('INSERT INTO books VALUES(?, ?, ?, ?)', book.to_list())

# conn.commit()
# conn.close()
# print('저장 완료')
import sqlite3

conn = sqlite3.connect('book.db')

cursor = conn.cursor()

cursor.execute('SELECT * FROM books')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

print('실행 완료')
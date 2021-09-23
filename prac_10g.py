import mysql.connector as mysql


db = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="mydata"
)

cursor = db.cursor()

query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"

values = [
    ("Peter","peter"),
    ("Amy","amy"),
    ("Michael","michael"),
    ("Hannah","hannah")
    ]

cursor.executemany(query, values)

db.commit()

print(cursor.rowcount, "was inserted.")
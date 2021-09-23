import mysql.connector as mysql


db = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="mydata"
)

cursor = db.cursor()

query = "UPDATE users SET name = 'Kareem' WHERE id = 1"

cursor.execute(query)

db.commit
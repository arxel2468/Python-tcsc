import mysql.connector as mysql


db = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="mydata"
)

cursor = db.cursor()

cursor.execute("ALTER TABLE users DROP id")


cursor.execute("DESC users")

print(cursor.fetchall())

import mysql.connector as mysql


db = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="mydata"
)

cursor = db.cursor()

cursor.execute("ALTER TABLE users ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")

cursor.execute("DESC users")
print(cursor.fetchall())

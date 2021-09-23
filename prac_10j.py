import mysql.connector as mysql


db = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="mydata"
)

cursor = db.cursor()

query = "SELECT * FROM users ORDER BY name"

cursor.execute(query)

records = cursor.fetchall()


print(records)
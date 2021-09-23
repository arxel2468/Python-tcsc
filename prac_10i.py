import mysql.connector as mysql


db = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="mydata"
)

cursor = db.cursor()

query = "SELECT * FROM users WHERE id = 4"

cursor.execute(query)

records = cursor.fetchall()

for records in records:
    print(records)
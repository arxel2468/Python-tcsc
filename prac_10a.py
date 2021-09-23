import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="mydata"
)

cursor = db.cursor()

cursor.execute("SHOW DATABASES")

databases = cursor.fetchall()

print(databases)

for databases in databases:
    print(databases)

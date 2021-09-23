import mysql.connector as mysql


db =  mysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydata"
)

cursor = db.cursor()

cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")
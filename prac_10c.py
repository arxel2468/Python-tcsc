import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="mydata"
)

cursor = db.cursor()

cursor.execute("DROP TABLE users")

cursor.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255))")

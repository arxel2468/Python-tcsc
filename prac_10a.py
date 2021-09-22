import mysql.connector
db = mysql.connector.connect(user='root', passwd='root', host='127.0.0.1', database='nit')
# prepare a cursor using cursor() method
cursor = db.cursor()
# Drop table if it already exist using execute() method
cursor.execute("Drop Table if exists Employee")
# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE
(FIRST NAME CHAR(20) NOT NULL,
AGE INT,
SEX CHAR(1),
INCOME FLOAT)"""
cursor.execute(sql)
print("Table Created Successfully");
# Disconnect from server 
db.close()

import mysql.connector
db = mysql.connector.connect(user='root', passwd='root', host='127.0.0.1', database='nit')
# prepare a cursor object usinf cursor() method
cursor = db.cursor()
# Prepare SQL query to insert a record into the database.
sql = """INSERT INTO EMPLOYEE (FIRST NAME,
LAST NAME,
AGE,
SEX,
INCOME)
VALUES('Nitesh','Shukla',20,'M',20000)"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    print("Table Created Successfully");
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any  error
    db.rollback()
# Disconnect from server 
db.close()
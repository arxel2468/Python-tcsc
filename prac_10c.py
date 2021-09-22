# Data Add
import mysql.connector
db = mysql.connector.connect(user='root', passwd='root', host='127.0.0.1', database='nit')
# prepare a cursor object usinf cursor() method
cursor = db.cursor()
# Prepare SQL query to insert a record into the database.
sql = """INSERT INTO EMPLOYEE (FIRST NAME, LAST NAME, AGE, SEX, INCOME
VALUES('%s','%s','%d','%c','%d')"""%('Ashwin','Mehta',23,'M',22000)
try:
    # Execute the SQL command
    cursor.execute(sql)
    print("Data Added Successfully");
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any  error
    db.rollback()
# Disconnect from server 
db.close()

# Delete Data
import mysql.connector
db = mysql.connector.connect(user='root', passwd='root', host='127.0.0.1', database='nit')
# prepare a cursor object usinf cursor() method
cursor = db.cursor()
# Prepare SQL query to insert a record into the database.
sql = "DELETE FROM EMPLOYEE WHERE AGE < '%d'"%(20)
try:
    # Execute the SQL command
    cursor.execute(sql)
    print("Data Deleted Successfully");
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any  error
    db.rollback()
# Disconnect from server 
db.close()

# Update Data
import mysql.connector
db = mysql.connector.connect(user='root', passwd='root', host='127.0.0.1', database='nit')
# prepare a cursor object usinf cursor() method
cursor = db.cursor()
# Prepare SQL query to insert a record into the database.
sql = "UPDATE EMPLOYEE SET AGE = AGE+1 WHERE SEX = '%c'"%('M')
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
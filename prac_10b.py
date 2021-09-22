import mysql.connector
db = mysql.connector.connect(user='root', passwd='root', host='127.0.0.1', database='nit')
# prepare a cursor object usinf cursor() method
cursor = db.cursor()
# Prepare SQL query to insert a record into the database.
sql = "SELECT * FROM EMPOLYEE WHERE INCOME > '%d'"%(1000)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # now print fetched result
        print("Fname = %s, Lname = %s, Age = %d, Sex = %s, Income = %d"(fname,lname,age,sex,income))
except:
    print("Error: Uable to fetch data")
# Disconnect from server 
db.close()
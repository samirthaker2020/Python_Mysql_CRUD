# This is a sample Python script.
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)


# mycursor.execute("CREATE DATABASE mydatabase")

# show if databse exsist or not

# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)

# table creation
# mycursor.execute("create table customers (cid INT AUTO_INCREMENT PRIMARY KEY ,name varchar(225) not null, city varchar(225) not null)")

def addrecord(name, city):
    mycursor = mydb.cursor()
    sql = "INSERT into customers VALUES (%s,%s,%s)"
    val = ("", name, city)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted sucessfully")
    mycursor.close()


def viewall():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM customers")
    mydata = mycursor.fetchall()
    mycursor.close()
    for x in mydata:
        print("Customer ID:" + str(x[0]))
        print("Customer Name:" + str(x[1]))
        print("Customer City:" + str(x[2]))


def remove(id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM customers WHERE cid=%s"
    print(sql)
    adr = (str(id),)

    mycursor.execute(sql, adr)
    mydb.commit()
    print(mycursor.rowcount, "record inserted deleted")
    mycursor.close()




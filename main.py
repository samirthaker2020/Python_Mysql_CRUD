# This is a sample Python script.
import mysql.connector
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

mycursor= mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")

# show if databse exsist or not

#mycursor.execute("SHOW DATABASES")
#for x in mycursor:
#   print(x)

# table creation
#mycursor.execute("create table customers (cid INT AUTO_INCREMENT PRIMARY KEY ,name varchar(225) not null, city varchar(225) not null)")

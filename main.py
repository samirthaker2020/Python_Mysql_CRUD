# This is a sample Python script.
import mysql.connector
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor= mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")

# show if databse exsist or not

mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
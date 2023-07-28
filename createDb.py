import mysql.connector as Myconn            #Myconn is an alias of mysql.connector

#==============================Establish Connection===========================

conn=Myconn.connect(host="localhost",               #conn is an object to connect python with the mysql database
                user="root",
                password="Himangshu@12345"
            )
# print(conn,"Connection established")

#==============================Database creating===========================

myconn_cursor=conn.cursor()               #myconn_cursor is an object and Using cursor() method inside conn object we can perform all sql operations in python.

myconn_cursor.execute("create database billing_db")
# Now using conn_cursor we can perform sql operations like insert update delete,etc. This execute method inside conn_cursor object we can pass sql queries
print("Database created successfully!")

#==============================Creating Table===========================

myconn_cursor=conn.cursor()
myconn_cursor.execute("create table ")

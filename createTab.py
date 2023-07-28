import mysql.connector as Myconn

conn=Myconn.connect(host="localhost",               #conn is an object to connect python with the mysql databas
                user="root",
                password="Himangshu@12345",
                database="Billing_db"               # Passing the database because all the tables wil be create inside this database. If we not giving then tables will be create inside root database
            )

myconn_cursor=conn.cursor()
myconn_cursor.execute("create table if not exists Bills(bill_number int primary key, customer_ph varchar(10), customer_name VARCHAR(80),total_amount int(10))")

print("Bills Table Created Successfully!")

myconn_cursor.execute("show tables")
for i in  myconn_cursor:
    print(i)
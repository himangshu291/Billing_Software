import mysql.connector as Myconn

conn=Myconn.connect(host="localhost",               #conn is an object to connect python with the mysql databas
                user="root",
                password="Himangshu@12345",
                database="Billing_db"               
            )

myconn_cursor=conn.cursor()
insert_query=("insert into Bills values(%s,%s,%s,%s)")              #In place of %s we will insert actual value
insert_value=(1000,"9749470744","Himangshu",500)
myconn_cursor.execute("insert into Bills values(%s,%s,%s,%s)",(1001,9749478594,"Anubrata",600))  
conn.commit()                                           #commit() is used to save the record inside the database. Without commit it cannot be saved or inserted.

print(myconn_cursor.rowcount,"Record inserted Successfully!")

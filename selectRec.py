import mysql.connector as Myconn

conn=Myconn.connect(host="localhost",               #conn is an object to connect python with the mysql databas
                user="root",
                password="Himangshu@12345",
                database="Billing_db"               
            )

myconn_cursor=conn.cursor()
myconn_cursor.execute("SELECT * FROM billing_db.Bills") 
    
for record in myconn_cursor.fetchall():
    print(record)

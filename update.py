import mysql.connector as Myconn

conn=Myconn.connect(host="localhost",               #conn is an object to connect python with the mysql database
                user="root",
                password="Himangshu@12345",
                database="Billing_db"               
            )

myconn_cursor=conn.cursor()
Updatedata="update Bills set bill_number=%s where customer_name=%s"
value=(1005,"sudip")
myconn_cursor.execute(Updatedata,value) 
conn.commit()       
print(myconn_cursor.rowcount,"record updated successfully")

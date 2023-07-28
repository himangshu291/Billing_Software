import mysql.connector as Myconn

conn=Myconn.connect(host="localhost",               #conn is an object to connect python with the mysql database
                user="root",
                password="Himangshu@12345",
                database="Billing_db"               
            )

myconn_cursor=conn.cursor()
deleteddata="delete from billing_db.Bills where customer_name=%s"
value=("subhankar,")
myconn_cursor.execute(deleteddata,value) 
conn.commit()       

print(myconn_cursor.rowcount,"record deleted successfully")

#To delete all the records use truncate
# deleteddata="truncate table billing_db.Bills"
# myconn_cursor.execute(deleteddata) 
# conn.commit() 
# print("All the records deleted successfully!")
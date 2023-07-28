import mysql.connector as Myconn

conn=Myconn.connect(host="localhost",               #conn is an object to connect python with the mysql databas
                user="root",
                password="Himangshu@12345",
                database="Billing_db"               
            )

myconn_cursor=conn.cursor()
insert_query=("insert into Bills values(%s,%s,%s,%s)")              #In place of %s we will insert actual value
insert_value=[(1002,"9749470859","Sudip",600),(1003,"9749496744","Sushmita",800),(1004,"9749470894","Subhankar",500)]                    #Through the list we can insert multiple values inside tuples
myconn_cursor.executemany(insert_query,insert_value)  
conn.commit()                                           #commit() is used to save the record inside the database. Without commit it cannot be saved.
        
print(myconn_cursor.rowcount,"Record inserted Successfully!")

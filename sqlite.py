import sqlite3

#define connection and cursor

# if we are refrencing a  database that doesnot exist a new data base will be created
connection=sqlite3.connect('store_transaction.db')


#cursor is used to interact with data using sql commands
cursor=connection.cursor()

#create stores table and checks if it exists if not creates a new

command1=""" CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)"""

#primary key means store id must be unique for each store

cursor.execute(command1)

#Create Purchase Table

command2=""" CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT, FOREIGN KEY(store_id) REFERENCES stores(store_id)) """

# we are refrencing the old table as store id as foreign key

cursor.execute(command2)

# create records add to stores and purchase

# add data to stores

cursor.execute("INSERT INTO stores VALUES (21,'MUMBAI, MUM')")
cursor.execute("INSERT INTO stores VALUES (95,'BANGLORE, BANG')")
cursor.execute("INSERT INTO stores VALUES (64,'DELHI, DEL')")

# add data to purchases

cursor.execute("INSERT INTO purchases VALUES (54,21,15.49)")
cursor.execute("INSERT INTO purchases VALUES (23,64,21.23)")
cursor.execute("INSERT INTO purchases VALUES (34,95,211.23)")


#get results

cursor.execute("SELECT * FROM purchases")

results=cursor.fetchall()
print(results)

#updating specific and delete

cursor.execute("UPDATE purchases SET total_cost=3.67 WHERE purchase_id=54")

#deleting row
cursor.execute("DELETE FROM purchases WHERE purchase_id=95")

result1=cursor.fetchall()
print(result1)

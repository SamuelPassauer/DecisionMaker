import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="adesso",
auth_plugin='mysql_native_password'
)

print(mydb)
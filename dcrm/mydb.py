import mysql.connector

dataBase = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'admin',
    passwd = 'Gts6500d!',

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
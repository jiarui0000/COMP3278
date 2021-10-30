import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", passwd="20010710", database="db")
cursor = connection.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version: ", data)

#create tables
# sql_file = open("./SQL/table.sql")
# sql_as_string = sql_file.read()
# cursor.execute(sql_as_string)
cursor.execute("CREATE TABLE Customer ( \
    customer_id VARCHAR(10) NOT NULL PRIMARY KEY, \
    name VARCHAR(50) NOT NULL, \
    gender VARCHAR(10) NOT NULL, \
    birthday DATE NOT NULL, \
    certification_type VARCHAR(10) NOT NULL, \
    id_number INT NOT NULL, \
    password VARCHAR(20) NOT NULL \
);")
cursor.execute("SHOW TABLES")
response = cursor.fetchone()
print("Response: \n", response)
connection.close()
# how to connect to a mysql database, create a table, insert into table, and query table
import mysql.connector

# define the database connection parameters
database = 'scriptdb'
host = 'localhost'
user = 'root'
password = 'password'

# establish a connection
cnx = mysql.connector.connect(
database = 'scriptdb',
host = 'localhost',
user = 'root',
password = 'password')

# create a cursor object
cursor = cnx.cursor()

# create a table
cursor.execute("""CREATE TABLE IF NOT EXIST staff(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, position VARCHAR(50) NOT NULL)""")

# inserting into table
cursor.execute("""INSERT INTO staff(name, position) VALUES ('agim given', 'software engineer')""")

# commit changes
cnx.commit()
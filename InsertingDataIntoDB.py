# Python code to demonstrate table creation and INSERT functions with SQL 
  
# importing your module= 
import sqlite3 
  
# connecting to the database  
connection = sqlite3.connect("myTable.db") 
  
# cursor  
crsr = connection.cursor() 
  
# SQL command to create a table in the database 
sql_command = """CREATE TABLE emp (  
staff_number INTEGER PRIMARY KEY,  
fname VARCHAR(20),  
lname VARCHAR(30),  
gender CHAR(1),  
joining DATE);"""

  
# SQL command to insert the data in the table 
sql_command = """INSERT INTO emp VALUES (6, "Eeee", "Eeee", "M", "2014-03-28");"""

# another SQL command to insert the data in the table 
sql_command = """INSERT INTO emp VALUES (7, "Dddd", "Dddd", "M", "1980-10-28");"""

#Command to execute SQL query
crsr.execute(select * from emp order by 1 desc) 
  
# To save the changes in the files. Never skip this. If we skip this, nothing will be saved in the database. 
connection.commit() 
  
# close the connection 
connection.close() 

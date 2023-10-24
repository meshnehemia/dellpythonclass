import sqlite3
conn = sqlite3.connect('example.db')
print("opened database Successfully")
# creating a table for storing information
conn.execute('''CREATE TABLE COMPANY1(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')
print("table created successfully")
conn.close()

import sqlite3

conn = sqlite3.connect("example.db")
print("connected successfully to the database")

conn.execute("UPDATE COMPANY1 SET ADDRESS = 'NAIROBI RUIRU ' WHERE NAME = 'Safaricom'")
conn.commit()
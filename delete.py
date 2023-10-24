import sqlite3
conn = sqlite3.connect("example.db")
print("opened database successfully")
conn.execute("DELETE FROM COMPANY1 where ID =2")
conn.commit()

import sqlite3

conn = sqlite3.connect("example.db")
print("opened database successfully ")
cursor = conn.execute("SELECT * FROM COMPANY1")
for row in cursor:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print("ADDRESS =", row[3])
    print("ID =", row[4])
    print("\n\n")
print("operation done successfully")

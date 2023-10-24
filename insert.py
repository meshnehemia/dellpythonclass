import  sqlite3
conn = sqlite3.connect("example.db")
print("opened database successfully")

conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(1,'Emobilis',7,'weslands',250000.00)");

conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(2,'Safaricom',7,'weslands',250000.00)");

conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(3,'Oracles',7,'weslands',250000.00)");

conn.execute("INSERT INTO COMPANY1(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(4,'Microsoft',7,'weslands',250000.00)");

conn.commit()
print("records created successfully")
conn.close()
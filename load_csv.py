import sqlite3 as sql
import pandas as pd

con = sql.connect("blockbusters.db")
cur = con.cursor()
tables = cur.fetchall()
# for (table_name, ) in tables:
#     print("1")
#     print(table_name)

cur.execute("""DELETE FROM `Catalog`;""")
cur.execute("""DELETE FROM Transactions;""")
cur.execute("""DELETE FROM Active_Rentals;""")
cur.execute("""DELETE FROM Customer;""")
cur.execute("""DELETE FROM Store;""")
cur.execute("""DELETE FROM Movie;""")
con.commit()


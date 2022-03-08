import sqlite3 as sql
import pandas as pd

con = sql.connect("blockbusters.db")
cur = con.cursor()
tables = cur.fetchall()
# for (table_name, ) in tables:
#     print("1")
#     print(table_name)


# Delete pre-existing rows
cur.execute("""DELETE FROM `Catalog`;""")
cur.execute("""DELETE FROM Transactions;""")
cur.execute("""DELETE FROM Active_Rentals;""")
cur.execute("""DELETE FROM Customer;""")
cur.execute("""DELETE FROM Store;""")
cur.execute("""DELETE FROM Movie;""")
con.commit()

# Read the csv files into pandas dataframe
catalog = pd.read_csv("data/Catalog.csv")
movie = pd.read_csv("data/Movies.csv")
customer = pd.read_csv("data/customer.csv")
store = pd.read_csv("data/store.csv")


# Create a function to iterate through pd data frame and insert into respective table
def row_processor(row, table_name, param):
    # print(row)
    temp_row = [str(x) for x in row.tolist()]
    for i in range(len(param)):
        if param[i] == "str":
            temp_row[i] = '\"' + temp_row[i] + '\"'

    new_row = ', '.join(temp_row)
    return 'INSERT INTO {} VALUES ({});'.format(table_name, new_row)

def pdtosql(data_frame, table_name, param):
    con = sql.connect("blockbusters.db")
    cur = con.cursor()
    args_list = []
    args_list.append(table_name)
    args_list.append(param)
    inserts = data_frame.apply(row_processor, args = args_list, axis = 1)
    for i in inserts:
        print(i)
        cur.execute(i)
    con.commit()


pdtosql(customer, "Customer", ["int", "str", "str"])
pdtosql(catalog, "Catalog", ["int", "int", "int", "int", "int"])
pdtosql(movie, "Movie", ["int", "str", "str", "str", "int", "str"])
pdtosql(store, "Store", ["int", "int", "str"])




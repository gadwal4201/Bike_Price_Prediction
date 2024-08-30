### database create and table create
# import mysql.connector as mc 
# conn = mc.connect(host = 'localhost', user = 'root', password = 'W7301@jqir3')


# if(conn.is_connected()):
#     print("hi")
# else:
#     print('error')

import sqlite3
conn = sqlite3.connect('bikedata.db')

query_to_create_table = """CREATE TABLE BikeDetails(
    owner INT, brand VARCHAR(40),kms_driven INT, 
    age INT, predicted_price INT)"""


cur = conn.cursor()
cur.execute(query_to_create_table)
print("Done")
cur.close()
conn.close()
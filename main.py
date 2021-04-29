import sqlite3
from sqlite3 import Error

database = sqlite3.connect("pythonsqlite.db")
cursor = database.cursor()

### QUERIES ###
def query(sqlCode):
  cursor.execute(sqlCode)
  result = cursor.fetchall()
  for row in result:
    print(row)
  print("\n")

def query(queryTitle, sqlCode):
  print(queryTitle)
  cursor.execute(sqlCode)
  result = cursor.fetchall()
  for row in result:
    print(row)
  print("\n")

query("Show all avialable GPUs in your invertory", "SELECT * FROM GPU")

query("GPUs with Clock Speed above 1.4MHz","SELECT GPU_Name FROM GPU WHERE Clock_Speed > 1400")

query("Show GPU quantity greater than 7 from the stock inventory","SELECT GPU_Name FROM STOCK_INVENTORY WHERE GPU_Quantity > 7")

query("Show customers from the city of Mondstadt or the state of Snezhnaya", "SELECT * FROM CUSTOMER_ACCOUNT WHERE City = 'Mondstadt' OR State = 'SN'")

query("Show all aftermarket cards ", "SELECT * FROM AFTERMARKET_INVENTORY")
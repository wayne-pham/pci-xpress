import sqlite3
from sqlite3 import Error

database = sqlite3.connect("pythonsqlite.db")
cursor = database.cursor()

############ QUERIES ############
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

#1
query("All avialable GPUs in your invertory", 
      "SELECT * FROM GPU")

#2
query("GPUs with Clock Speed above 1.4MHz",
      "SELECT GPU_Name FROM GPU WHERE Clock_Speed > 1400")

#3
query("GPU quantity greater than 7 from the stock inventory",
      "SELECT GPU_Name FROM STOCK_INVENTORY WHERE GPU_Quantity > 7")

#4
query("Customers from the city of Mondstadt or the state of Snezhnaya", 
      "SELECT * FROM CUSTOMER_ACCOUNT WHERE City = 'Mondstadt' OR State = 'SN'")

#5
query("All aftermarket cards", 
      "SELECT GPU_Name FROM AFTERMARKET_INVENTORY WHERE GPU_Quantity > 7 ORDER BY GPU_Name ASC")

#6
query("GPUs with VRAM higher than 10GB", 
      "SELECT GPU_Name FROM GPU WHERE VRAM > 10 ORDER BY GPU_Name DESC")

#7
query("GPU from stock and aftermarket that are similar in name and quantity", 
      "SELECT STOCK_INVENTORY.GPU_Name, STOCK_INVENTORY.GPU_Quantity FROM STOCK_INVENTORY INNER JOIN AFTERMARKET_INVENTORY ON STOCK_INVENTORY.Store_Name = AFTERMARKET_INVENTORY.Store_Name")

#8

#9

#10
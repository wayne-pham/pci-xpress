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
query("All available GPUs in your inventory",
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
query("What customers used a credit card to make a purchase at PCI-Xpress? For security reasons list the email only and type of payment.",
      "SELECT CUSTOMER_ACCOUNT.Email, CUSTOMER.Payment_Method FROM CUSTOMER_ACCOUNT INNER JOIN CUSTOMER ON CUSTOMER_ACCOUNT.Account_ID = CUSTOMER.ID WHERE CUSTOMER.Payment_Method LIKE 'CREDIT'")

#8
query("What Employees make more than $100.00?", 
      "SELECT Name, Wage FROM EMPLOYEE WHERE Wage > 100")

#9
query("Which customers purchased more than 2 items from PCI-Xpress?",
      "SELECT CUSTOMER_ACCOUNT.Email, CUSTOMER.Items_Purchased FROM CUSTOMER INNER JOIN CUSTOMER_ACCOUNT ON CUSTOMER_ACCOUNT.Account_ID = CUSTOMER.ID WHERE CUSTOMER.Items_Purchased > 2")

#10
query("What GPU Manufacturers are in Santa Clara?",
      "SELECT Name, Contact_Number FROM MANUFACTURER WHERE City LIKE 'Santa Clara' ORDER BY Name ASC")

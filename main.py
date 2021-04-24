import sqlite3
from sqlite3 import Error

database = sqlite3.connect("pythonsqlite.db")
cursor = database.cursor()

### CREATE TABLES ###
cursor.execute("DROP TABLE IF EXISTS STORE")

store = """
CREATE TABLE STORE
(
  Store_Name VARCHAR(100) NOT NULL,
  Address_line_1 VARCHAR(100) NOT NULL,
  City VARCHAR(100) NOT NULL,
  State VARCHAR(100) NOT NULL,
  Zip INT NOT NULL,
  Phone_Number INT NOT NULL,
  PRIMARY KEY (Store_Name),
  UNIQUE (Phone_Number)
); """
cursor.execute(store)

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
employee = """ 
CREATE TABLE EMPLOYEE
(
  ID INT NOT NULL,
  Name VARCHAR(100) NOT NULL,
  Wage FLOAT NOT NULL,
  Address_line_1 VARCHAR(100) NOT NULL,
  City VARCHAR(100) NOT NULL,
  State VARCHAR(100) NOT NULL,
  Zip INT NOT NULL,
  DOB VARCHAR(100) NOT NULL,
  Store_Name VARCHAR(100) NOT NULL,
  PRIMARY KEY (ID),
  FOREIGN KEY (Store_Name) REFERENCES STORE(Store_Name)
); """
cursor.execute(employee)


cursor.execute("DROP TABLE IF EXISTS CUSTOMER_ACCOUNT")
cursor.execute("DROP TABLE IF EXISTS AFTERMARKET_INVENTORY")
cursor.execute("DROP TABLE IF EXISTS store MANUFACTURER")
cursor.execute("DROP TABLE IF EXISTS store STOCK_INVENTORY")
cursor.execute("DROP TABLE IF EXISTS store CUSTOMER")
cursor.execute("DROP TABLE IF EXISTS store GPU")


database.commit()


# ### INSERT DATA ###

# ### QUERIES ###
import sqlite3
from sqlite3 import Error

database = sqlite3.connect("pythonsqlite.db")
cursor = database.cursor()

### CREATE TABLES ###

# Store
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

# Employee
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

# Customer Account
cursor.execute("DROP TABLE IF EXISTS CUSTOMER_ACCOUNT")
customer_account = """
CREATE TABLE CUSTOMER_ACCOUNT
(
  Account_ID INT NOT NULL,
  Email VARCHAR(100) NOT NULL,
  Phone_Number INT NOT NULL,
  Address_line_1 VARCHAR(100) NOT NULL,
  City VARCHAR(100) NOT NULL,
  State VARCHAR(100) NOT NULL,
  Zip INT NOT NULL,
  Name VARCHAR(100) NOT NULL,
  DOB VARCHAR(100) NOT NULL,
  PRIMARY KEY (Account_ID)
); """
cursor.execute(customer_account)



# Aftermarket Inventory
cursor.execute("DROP TABLE IF EXISTS AFTERMARKET_INVENTORY")
aftermarket_inventory = """
CREATE TABLE AFTERMARKET_INVENTORY
(
  GPU_Name VARCHAR(100) NOT NULL,
  GPU_Quantity INT NOT NULL,
  Store_Name VARCHAR(100) NOT NULL,
  PRIMARY KEY (GPU_Name),
  FOREIGN KEY (Store_Name) REFERENCES STORE(Store_Name)
); """

# Manufacturer 
cursor.execute("DROP TABLE IF EXISTS MANUFACTURER")
manufacturer = """
CREATE TABLE MANUFACTURER
(
  Name VARCHAR(100) NOT NULL,
  Contact_Number INT NOT NULL,
  Address_line_1 VARCHAR(100) NOT NULL,
  City VARCHAR(100) NOT NULL,
  State VARCHAR(100) NOT NULL,
  Zip INT NOT NULL,
  Store_Name VARCHAR(100) NOT NULL,
  PRIMARY KEY (Name),
  FOREIGN KEY (Store_Name) REFERENCES STORE(Store_Name),
  UNIQUE (Contact_Number)
); """
cursor.execute(manufacturer)

# Stock Inventory
cursor.execute("DROP TABLE IF EXISTS STOCK_INVENTORY")
stock_inventory = """
CREATE TABLE STOCK_INVENTORY
(
  GPU_Name VARCHAR(100) NOT NULL,
  GPU_Quantity INT NOT NULL,
  Store_Name VARCHAR(100) NOT NULL,
  PRIMARY KEY (GPU_Name),
  FOREIGN KEY (Store_Name) REFERENCES STORE(Store_Name)
); """
cursor.execute(stock_inventory)

# Customer
cursor.execute("DROP TABLE IF EXISTS CUSTOMER")
customer = """
CREATE TABLE CUSTOMER
(
  ID INT NOT NULL,
  Payment_Method VARCHAR(100) NOT NULL,
  Payment_Amount FLOAT NOT NULL,
  Items_Purchased INT NOT NULL,
  Card_Number INT NULL,
  Store_Name VARCHAR(100),
  PRIMARY KEY (ID),
  FOREIGN KEY (Store_Name) REFERENCES STORE(Store_Name),
  FOREIGN KEY (ID) REFERENCES CUSTOMER_ACCOUNT(Account_ID)
); """
cursor.execute(customer)

# GPU
cursor.execute("DROP TABLE IF EXISTS GPU")
gpu = """
CREATE TABLE GPU
(
  GPU_Name VARCHAR(100) NOT NULL,
  GPU_Retail_Price FLOAT NOT NULL,
  GPU_Wholesale_Price FLOAT NOT NULL,
  Architecture VARCHAR(100) NOT NULL,
  Power_Requirement INT NOT NULL,
  VRAM INT NOT NULL,
  Clock_Speed INT NOT NULL,
  Manufacturer VARCHAR(100) NOT NULL,
  PRIMARY KEY (GPU_Name),
  FOREIGN KEY (GPU_Name) REFERENCES STOCK_INVENTORY(GPU_Name),
  FOREIGN KEY (GPU_Name) REFERENCES AFTERMARKET_INVENTORY(GPU_Name)
); """
cursor.execute(gpu)

database.commit()


# ### INSERT DATA ###




# ### QUERIES ###
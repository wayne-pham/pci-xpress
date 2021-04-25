import sqlite3
from sqlite3 import Error

database = sqlite3.connect("pythonsqlite.db")
cursor = database.cursor()

############ TABLES #############

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
cursor.execute(aftermarket_inventory)

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



############ INSERT DATA #############

# Store
cursor.execute("INSERT INTO STORE VALUES(?, ?, ?, ?, ?, ?);", ('PCIXpress','1234 Capacitor Rd','Indianapolis','IN', 12345, 1234567890))

# Stock Inventory
cursor.execute("INSERT INTO STOCK_INVENTORY VALUES(?,?,?);", ('RTX 3090 Founders Edition', 10, 'PCIXpress'))
cursor.execute("INSERT INTO STOCK_INVENTORY VALUES(?,?,?);", ('RTX 3080 Founders Edition', 9, 'PCIXpress'))
cursor.execute("INSERT INTO STOCK_INVENTORY VALUES(?,?,?);", ('RTX 3070 Founders Edition', 8, 'PCIXpress'))
cursor.execute("INSERT INTO STOCK_INVENTORY VALUES(?,?,?);", ('RTX 3060 Founders Edition', 7, 'PCIXpress'))
cursor.execute("INSERT INTO STOCK_INVENTORY VALUES(?,?,?);", ('RTX 3060 Ti Founders Edition', 6, 'PCIXpress'))
cursor.execute("INSERT INTO STOCK_INVENTORY VALUES(?,?,?);", ('Radeon RX 6700XT', 5, 'PCIXpress'))

# Aftermarket Inventory
cursor.execute("INSERT INTO AFTERMARKET_INVENTORY VALUES(?,?,?);", ('RTX 3090 Founders Edition', 10, 'PCIXpress'))
cursor.execute("INSERT INTO AFTERMARKET_INVENTORY VALUES(?,?,?);", ('RTX 3080 Founders Edition', 9, 'PCIXpress'))
cursor.execute("INSERT INTO AFTERMARKET_INVENTORY VALUES(?,?,?);", ('RTX 3070 Founders Edition', 8, 'PCIXpress'))
cursor.execute("INSERT INTO AFTERMARKET_INVENTORY VALUES(?,?,?);", ('RTX 3060 Founders Edition', 7, 'PCIXpress'))
cursor.execute("INSERT INTO AFTERMARKET_INVENTORY VALUES(?,?,?);", ('RTX 3060 Ti Founders Edition', 6, 'PCIXpress'))
cursor.execute("INSERT INTO AFTERMARKET_INVENTORY VALUES(?,?,?);", ('Radeon RX 6700XT', 5, 'PCIXpress'))

# GPU
cursor.execute("INSERT INTO GPU VALUES(?,?,?,?,?,?,?,?);", ('RTX 3090 Founders Edition', 1500.0, 600.0, 'Ampere', 1000, 24, 1395, 'Nvidia'))
cursor.execute("INSERT INTO GPU VALUES(?,?,?,?,?,?,?,?);", ('RTX 3080 Founders Edition', 700.0, 280.0, 'Ampere', 750, 10, 1440, 'Nvidia'))
cursor.execute("INSERT INTO GPU VALUES(?,?,?,?,?,?,?,?);", ('RTX 3070 Founders Edition', 500.0, 200.0, 'Ampere', 650, 8, 1500, 'Nvidia'))
cursor.execute("INSERT INTO GPU VALUES(?,?,?,?,?,?,?,?);", ('RTX 3060 Founders Edition', 330.0, 132.0, 'Ampere', 550, 12, 1320, 'Nvidia'))
cursor.execute("INSERT INTO GPU VALUES(?,?,?,?,?,?,?,?);", ('RTX 3060 Ti Founders Edition', 400.0, 160.0, 'Ampere', 600, 8, 1410, 'Nvidia'))
cursor.execute("INSERT INTO GPU VALUES(?,?,?,?,?,?,?,?);", ('Radeon RX 6700XT', 479.0, 287.0, 'Big Navi', 600, 12, 2321, 'AMD'))

# Customer
cursor.execute("INSERT INTO CUSTOMER VALUES(?,?,?,?,?,?);", (1, 'CREDIT', 899.00, 1, 5161889457891231, 'PCIXpress'))
cursor.execute("INSERT INTO CUSTOMER VALUES(?,?,?,?,?,?);", (2, 'DEBIT', 1800.00, 2, 9875458612258549, 'PCIXpress'))
cursor.execute("INSERT INTO CUSTOMER VALUES(?,?,?,?,?,?);", (3, 'CREDIT', 3000.00, 3, 5421649879865465, 'PCIXpress'))
cursor.execute("INSERT INTO CUSTOMER VALUES(?,?,?,?,?,?);", (4, 'CREDIT', 4000.00, 4, 8916854489491213, 'PCIXpress'))
cursor.execute("INSERT INTO CUSTOMER VALUES(?,?,?,?,?,?);", (5, 'DEBIT', 500.00, 1, 5454897425689864, 'PCIXpress'))

# Customer Account
cursor.execute("INSERT INTO CUSTOMER_ACCOUNT VALUES(?,?,?,?,?,?,?,?,?);", (1, 'Blub@pcixpress.com', 1234567, '1234 Nulaxy Ave', 'Indianapolis', 'IN', 46589, 'Blub', '12/11/2000')) 
cursor.execute("INSERT INTO CUSTOMER_ACCOUNT VALUES(?,?,?,?,?,?,?,?,?);", (2, 'Klee@pcixpress.com', 7654321, '6456 Jumpty dumpty Rd', 'Mondstadt', 'MD', 97897, 'Klee', '12/11/2010')) 
cursor.execute("INSERT INTO CUSTOMER_ACCOUNT VALUES(?,?,?,?,?,?,?,?,?);", (3, 'Nora@pcixpress.com', 6762655, '4564 Imaginary ln', 'Mondstadt', 'MD', 56486, 'Nora', '12/11/2010')) 
cursor.execute("INSERT INTO CUSTOMER_ACCOUNT VALUES(?,?,?,?,?,?,?,?,?);", (4, 'Fatooey@pcixpress.com', 1666666, '4898 Tsarista Ct', 'Zapolyarny Palace', 'SN', 79786, 'Fatooey', '12/11/1990')) 
cursor.execute("INSERT INTO CUSTOMER_ACCOUNT VALUES(?,?,?,?,?,?,?,?,?);", (5, 'Lapis@pcixpress.com', 1564897, '6878 Jade ln', 'Minlin', 'LY', 45644, 'Lapis', '12/11/1000'))

# Employee
cursor.execute("INSERT INTO EMPLOYEE VALUES(?,?,?,?,?,?,?,?,?);", (1, 'Wayne Pham', 200.00, '3432 West Haven Dr.', 'Indianapolis', 'IN', 47899, '10/12/1999', 'PCIXpress'))
cursor.execute("INSERT INTO EMPLOYEE VALUES(?,?,?,?,?,?,?,?,?);", (2, 'Samip Vaidh', 200.00,'4654 Sugar Weight Dr.', 'Indianapolis', 'IN', 56481, '05/28/1994', 'PCIXpress'))

# Manufacturer
cursor.execute("INSERT INTO MANUFACTURER VALUES(?,?,?,?,?,?,?);", ('Nvidia', 18007976530, '2788 San Tomas Expressway', 'Santa Clara', 'CA', 95050, 'PCIXpress'))
cursor.execute("INSERT INTO MANUFACTURER VALUES(?,?,?,?,?,?,?);", ('AMD', 18772841566, '2485 Augustine Road', 'Santa Clara', 'CA', 95054, 'PCIXpress'))

database.commit()

### QUERIES ###

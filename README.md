# 512_BigBucks_Proj_Pkg Documentation

## Preview

This is for FINTECH 512 Group Project Backend Supabase Database.

We are using Supabase PostgresSQL database for our project. For more information, visit [Supabase Website](https://supabase.com/).

## Database Structure

### Tables : Customer_Information, Customer_Password, Stock_Name, Stock_Price_Daily_Data, Transaction_Records

### 1. Customer_Information

| Column Name     |     Type      |    Keys     |
| :-------------- | :-----------: | :---------: |
| customer_id     |     `int`     | Primary Key |
| first_name      |    `text`     |     `-`     |
| last_name       |    `text`     |     `-`     |
| phone_number    |     `int`     |     `-`     |
| email_address   |    `text`     |     `-`     |
| user_name       |    `text`     |     `-`     |
| password        |    `text`     |     `-`     |
| created_at      | `timestamptz` |     `-`     |
| account_balance |    `float`    |     `-`     |

### 2. Stock_Information

| Column Name     |  Type  |    Keys     |
| :-------------- | :----: | :---------: |
| stock_symbol    | `text` | Primary Key |
| stock_full_name | `text` |     `-`     |
| exchange        | `text` |     `-`     |
| sector          | `text` |     `-`     |
| industry        | `text` |     `-`     |
### 3.  Stock_Price_Daily_Data

| Column Name    |  Type   |    Keys     |
| :------------- | :-----: | :---------: |
| ids   | `int` | Primary Key |
| stock_symbol   | `text`  | `-` |
| date           | `date`  |     `-`     |
| open           | `float` |     `-`     |
| high           | `float` |     `-`     |
| low            | `float` |     `-`     |
| close          | `float` |     `-`     |
| adjusted_close | `float` |     `-`     |
| volume         |  `int`  |     `-`     |

### 4. Transaction_Records

| Column Name          |    Type     |                       Keys                        |
| :------------------- | :---------: | :-----------------------------------------------: |
| transaction_id       |    `int`    |                    Primary Key                    |
| customer_id          |    `int`    | Foreign Key to `Customer_Information.customer_id` |
| transaction_date     | `timestamp` |                        `-`                        |
| condition            |  ``text``   |                        `-`                        |
| stock_symbol         |  `varchar`  |                        `-`                        |
| num_shares           |    `int`    |                        `-`                        |
| stock_price_realtime |   `float`   |                        `-`                        |
### 5.  SP500_Index

| Column Name    |  Type   |    Keys     |
| :------------- | :-----: | :---------: |
| date | `date` | Primary Key |
| close | `float` | `-` |

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `bigbucks_db`.

```bash
pip install bigbucks-db
```

Note : If you want to know more information about this package, please go visit [official website](https://pypi.org/project/bigbucks-db/).

## Functions

### 1. Database Update
- Update Customer_Information

```python
# Example Code
# below are information needs to be included
from bigbucks_db import *
# Enter database url and keys here
SUPABASE_URL = ""
KEYS = ""
STOCK_API_KEYS = ""
db = Table_Updates(SUPABASE_URL, KEYS, STOCK_API_KEYS)

# first_name : str, last_name : str, phone_number : int, email_address : str, user_name : str, password : str
tmp = db.update_customer_info("Sam", "Jay", 2892892893, "duke@email", "Jay_invest", "duke512")
# tmp[0] is the table name, tmp[1] is the data needs to be updated
db.supabase_insert_function(tmp[0], tmp[1]) 
print(tmp)
```

- Update Stock_Information 

  Note : this function has already integrated to update Transaction_Records function

```python
# Example Code
# below are information needs to be included
from bigbucks_db import *
# Enter database url and keys here
SUPABASE_URL = ""
KEYS = ""
STOCK_API_KEYS = ""
db = Table_Updates(SUPABASE_URL, KEYS, STOCK_API_KEYS)

# stock_symbol : str, stock_full_name : str, exchange : str, sector : str, industry : str
tmp = db.update_stock_details("AAPL","Apple","NYSE","Tech","COMPUTER & OFFICE EQUIPMENT")
# tmp[0] is the table name, tmp[1] is the data needs to be updated
db.supabase_insert_function(tmp[0], tmp[1]) 
print(tmp)
```

- Update Stock_Price_Daily_Data

  Note : this function has already integrated to update 5 years stock price data function (part3)

```python
# Example Code
# below are information needs to be included
from bigbucks_db import *
# Enter database url and keys here
SUPABASE_URL = ""
KEYS = ""
STOCK_API_KEYS = ""
db = Table_Updates(SUPABASE_URL, KEYS, STOCK_API_KEYS)

# stock_symbol : str, date, open_ : float, high : float, low : float, close : float, adjusted_close : float, volume : int
tmp = db.update_stock_daily_price("AAPL", "2022-12-15",122.12,112.89,122.02,132.12,122.73,231231)
# tmp[0] is the table name, tmp[1] is the data needs to be updated
db.supabase_insert_function(tmp[0], tmp[1]) 
print(tmp)
```

- Update Transaction_Records

  Note : by running this function, both Stock_Information table and Customer_Information's account balance will be also synchronized, now can also update the Stock_Price_Daily_Data at the same time

```python
# Example Code
# below are information needs to be included
from bigbucks_db import *
# Enter database url and keys here
SUPABASE_URL = ""
KEYS = ""
STOCK_API_KEYS = ""
db = Table_Updates(SUPABASE_URL, KEYS, STOCK_API_KEYS)

# Alpha Vantage API keys goes here
stock = Buy_And_Sell(STOCK_API_KEY)
price = stock.get_realtime_stock_price(stock_symbol) # "AAPL" in this case

# user_name : str, stock_symbol : str, num_shares : int, stock_price_realtime : float, condition : str
tmp = db.update_transaction_records("Jay_invest", "buy", "AAPL", 123, price) # condition be "sell" or "buy"
# tmp[0] is the table name, tmp[1] is the data needs to be updated
db.supabase_insert_function(tmp[0], tmp[1]) 
print(tmp)
```

### 2. Get Realtime Stock Data 

```python
from bigbucks_db import *

# Enter stock keys here
STOCK_API_KEYS = ""
objs = Buy_And_Sell(STOCK_API_KEYS)

# realtime stock data within 1 mins interval
stock_symbol = ""
price = objs.get_realtime_stock_price(stock_symbol)
print(price)
# or you could use backup function to get price in case above function fail
price2 = objs.realtime_price_bkp(stock_symbol)
print(price2)
```

### 3. Update 5 Years Stock Price Data 

​	Note : only when customers buy stocks to implement this function since it will only go though the stock_information table

```python
# Example Code
# below are information needs to be included
from bigbucks_db import *
# Enter database url and keys here
SUPABASE_URL = ""
KEYS = ""
STOCK_API_KEYS = ""
stock = Stock_Data(SUPABASE_URL, KEYS, STOCK_API_KEYS)

# update all stock price goes here - if all symbols already existed, message "stock symbol already exists" will show up
data = stock.update_all_stock_price()
```

### 4. View Table Data

- Set up object

```python
# Example Code
# below are information needs to be included
from bigbucks_db import *
# Enter database url and keys here
SUPABASE_URL = ""
KEYS = ""
objs = Table_View(SUPABASE_URL, KEYS)
```

- View all data without querying

```python
# table_name : str 
# select from "Customer_Information", "Stock_Information", "Stock_Price_Daily_Data", "Transaction_Records"
table_name = "Transaction_Records"
data = objs.view_table_data(table_name)
print(data)
```

​       Example results : 
```bash
[{'transaction_id': 7, 'customer_id': 6, 'transaction_date': '2023-04-01T20:35:29.239042', 'stock_symbol': 'AAPL', 'num_shares': 100, 'stock_price_realtime': 164.839996337891, 'condition': 'buy'}, {'transaction_id': 10, 'customer_id': 6, 'transaction_date': '2023-04-01T20:37:52.832943', 'stock_symbol': 'AAPL', 'num_shares': 100, 'stock_price_realtime': 164.839996337891, 'condition': 'sell'}]
```

- View stock price with querying
```python
# symbol_name : str
symbol_name = "AAPL"
data = objs.view_symbol_price_data(symbol_name)
print(data)
```

​       Example results : 
```bash
[{'stock_symbol': 'AAPL', 'date': '2018-04-10', 'open': 173, 'high': 174, 'low': 171.53, 'close': 173.25, 'adjusted_close': 41.2348154406459, 'volume': 28614241, 'ids': 1254}, {'stock_symbol': 'AAPL', 'date': '2018-04-09', 'open': 169.88, 'high': 173.09, 'low': 169.85, 'close': 170.05, 'adjusted_close': 40.4731911439067, 'volume': 29017718, 'ids': 1255}]
```

### 5. View Customers' Transaction Records & Current Portfolio

Note : those are back up functions

- View customers' transaction records

```python
# Example Code
# below are information needs to be included
from bigbucks_db import *
# Enter database url and keys here
SUPABASE_URL = ""
KEYS = ""

objs = Table_View(SUPABASE_URL, KEYS)
# user_name : str
user_name = "Jeffd"
results = objs.view_customer_transaction(user_name)
print(results)
```

​        Example results : 

```bash
{'AAPL': [('buy', 100, 164.839996337891), ('sell', 100, 164.839996337891)], 'IBM': [('sell', 100, 164.839996337891), ('buy', 100, 164.839996337891), ('buy', 100, 131.070007324219)]}
```
- View customers' current portfolio

```python
# Example Code
# below are information needs to be included
from bigbucks_db import *
# Enter database url and keys here
SUPABASE_URL = ""
KEYS = ""

objs = Table_View(SUPABASE_URL, KEYS)
# user_name : str
user_name = "Jeffd"
results = objs.view_customer_portfolio(user_name)
print(results)
```

​        Example results : 

```bash
{'IBM': {'shares': 100}}
```
### 6. Update 5 Years SP500 

Note : this is only for demostration and no need to run this code - all data has already updated

```python
# Example Code
# below are information needs to be included
from bigbucks_db import *
# Enter database url and keys here
SUPABASE_URL = ""
KEYS = ""
STOCK_API_KEYS = ""
sp500 = SP500(SUPABASE_URL, KEYS, STOCK_API_KEYS)
updates = sp500.update_sp_500()

# you can also get realtime SP500 data
data = realtime_sp500()
print(data)
```

## Other

### Note : 

### -  `user_name` is unique 
### -  `account_balance` is set default to 1,000,000 as new customer registered



## Update

Use the package manager [pip](https://pip.pypa.io/en/stable/) to upgrade `bigbucks-db`.


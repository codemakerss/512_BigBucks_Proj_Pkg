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

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `bigbucks_db`.

```bash
pip install bigbucks-db
```

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

  Note : by running this function, both Stock_Information table and Customer_Information's account balance will be also synchronized

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

### 3. Update 5 years stock price data 

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




## Other

### Note : 

### -  `user_name` is unique 
### -  `account_balance` is set default to 1,000,000 as new customer registered



## Update

Use the package manager [pip](https://pip.pypa.io/en/stable/) to upgrade `bigbucks_db`.


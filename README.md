# 512_BigBucks_Proj_Pkg Documentation

## Preview

This is for FINTECH 512 Group Project Backend Supabase Database.

We are using Supabase PostgresSQL database for our project. For more information, visit [Supabase Website](https://supabase.com/).

## Database Structure

### Tables : Customer_Information, Customer_Password, Stock_Name, Stock_Price_Daily_Data, Transaction_Records

### 1. Customer_Information

| Column Name   |     Type      |    Keys     |
| :------------ | :-----------: | :---------: |
| customer_id   |     `int`     | Primary Key |
| first_name    |    `text`     |     `-`     |
| last_name     |    `text`     |     `-`     |
| phone_number  |     `int`     |     `-`     |
| email_address |    `text`     |     `-`     |
| user_name     |    `text`     |     `-`     |
| password      |    `text`     |     `-`     |
| created_at    | `timestamptz` |     `-`     |

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
| stock_symbol   |  `int`  | Primary Key |
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
| stock_symbol         |  `varchar`  |                        `-`                        |
| num_shares           |    `int`    |                        `-`                        |
| stock_price_realtime |   `float`   |                        `-`                        |


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `bigbucks_db`.

```bash
pip install bigbucks_db
```

## Functions

- Set up class objects here

```python
from bigbucks_db import *

# Enter database url and keys here
SUPABASE_URL = ""
KEYS = ""
db = Table_Updates(SUPABASE_URL, KEYS)
```

- Update Customer_Information

```python
# Example Code
# below are information needs to be included
# first_name : str, last_name : str, phone_number : int, email_address : str, user_name : str, password : str
tmp = db.update_stock_name("Sam", "Jay", 2892892893, "duke@email", "Jay_invest", "duke512")
# tmp[0] is the table name, tmp[1] is the data needs to be updated
db.supabase_insert_function(tmp[0], tmp[1]) 
print(tmp)
```

- Update Stock_Information

```python
# Example Code
# below are information needs to be included
# stock_symbol : str, stock_full_name : str, exchange : str, sector : str, industry : str
tmp = db.update_stock_name("AAPL","Apple","NYSE","Tech","COMPUTER & OFFICE EQUIPMENT")
# tmp[0] is the table name, tmp[1] is the data needs to be updated
db.supabase_insert_function(tmp[0], tmp[1]) 
print(tmp)
```

- Update Stock_Price_Daily_Data

```python
# Example Code
# below are information needs to be included
# stock_symbol : str, date, open_ : float, high : float, low : float, close : float, adjusted_close : float, volume : int
tmp = db.update_stock_daily_price("AAPL", "2022-12-15",122.12,112.89,122.02,132.12,122.73,231231)
# tmp[0] is the table name, tmp[1] is the data needs to be updated
db.supabase_insert_function(tmp[0], tmp[1]) 
print(tmp)
```

- Update Transaction_Records

```python
# Example Code
# below are information needs to be included
# user_name : str, stock_symbol : str, num_shares : int, stock_price_realtime : float
tmp = db.update_transaction_records("Jay_invest", "AAPL", 123, 125.19)
# tmp[0] is the table name, tmp[1] is the data needs to be updated
db.supabase_insert_function(tmp[0], tmp[1]) 
print(tmp)
```

## Other

### Note : `user_name` is unique 

## Update

Use the package manager [pip](https://pip.pypa.io/en/stable/) to upgrade `bigbucks_db`.


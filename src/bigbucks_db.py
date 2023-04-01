import sys
# import requests
# import json
# import pendulum
# import time

# Do not show error traceback
sys.tracebacklimit=0
# Check if all packages installed 
try:
    import requests
except ImportError as e:
    print("Package <requests> needed to be installed before getting data ! ")
    raise e 

try:
    import json
except ImportError as e:
    print("Package <json> needed to be installed before getting data ! ")
    raise e 

try:
    import pendulum
except ImportError as e:
    print("Package <pendulum> needed to be installed before getting data ! ")
    raise e 

try:
    import time
except ImportError as e:
    print("Package <time> needed to be installed before getting data ! ")
    raise e 

try:
    import yfinance as yf
except ImportError as e:
    print("Package <yfinance> needed to be installed before getting data ! ")
    raise e

try:
    import pandas as pd
except ImportError as e:
    print("Package <pandas> needed to be installed before getting data ! ")
    raise e

TABLE_NAME = ["Customer_Information", "Customer_Password", "Stock_Name", "Stock_Price_Daily_Data", "Transaction_Records"]

# Customer_Information = ["customer_id", "first_name", "last_name", "phone_number", "email_address", "user_name", "password", "created_at", "account_balance"]
# Customer_Password = ["customer_id", "created_at", "password"]
# Stock_Name = ["stock_symbol", "stock_full_name", "exchange", "sector", "industry"]
# Stock_Price_Daily_Data = ["stock_symbol", "date", "open", "high", "low", "close", "adjusted_close", "volume"]
# Transaction_Records = ["transaction_id", "customer_id", "transaction_date", "stock_symbol", "num_shares", "stock_price_realtime"]


class Table_Updates(object):
	def __init__(self, SUPABASE_URL, KEYS):
		self.url = SUPABASE_URL
		self.keys = KEYS

	# customers information data updated 
	def update_customer_info(self, first_name : str, last_name : str, phone_number : int, email_address : str, user_name : str, password : str):
		customer_info = {}
		customer_info["first_name"] = first_name
		customer_info["last_name"] = last_name
		customer_info["phone_number"] = phone_number
		customer_info["email_address"] = email_address
		customer_info["user_name"] = user_name
		customer_info["password"] = password
		customer_info["account_balance"] = 1000000.00

		return "Customer_Information", customer_info

	# get the customer id from Customer_Information
	def get_customer_id(self, table_name : str, user_name : str):
		# by unique name of username and customer id 
		try:
			api_url = self.url + "/rest/v1/" + table_name + "?user_name=eq." + user_name

			parameters =  {"apikey":self.keys}

			response = requests.get(url =api_url, params = parameters)
			data = json.loads(response.text)

			return data[0]["customer_id"]

		except:
			print("Fail to get data from supabse datatbase. ")

	# provides stock details 
	def update_stock_details(self, stock_symbol : str, stock_full_name : str, exchange : str, sector : str, industry : str):
		stock_name = {}
		stock_name["stock_symbol"] = stock_symbol
		stock_name["stock_full_name"] = stock_full_name
		stock_name["exchange"] = exchange
		stock_name["sector"] = sector
		stock_name["industry"] = industry

		return "Stock_Information", stock_name

	# daily price
	def update_stock_daily_price(self, stock_symbol : str, date, open_ : float, high : float, low : float, close : float, adjusted_close : float, volume : int):
		stock_price = {}
		stock_price["stock_symbol"] = stock_symbol
		stock_price["date"] = date
		stock_price["open"] = open_
		stock_price["high"] = high
		stock_price["low"] = low
		stock_price["close"] = close
		stock_price["adjusted_close"] = adjusted_close
		stock_price["volume"] = volume

		return "Stock_Price_Daily_Data", stock_price

	# transaction - auto update datetime
	def update_transaction_records(self, user_name : str, condition : str, stock_symbol : str, num_shares : int, stock_price_realtime : float):
		# condition here means buy or sell action
		# user_name is required to get the customer id
		customer_id = self.get_customer_id("Customer_Information", user_name)

		transactions = {}
		transactions["customer_id"] = customer_id
		transactions["condition"] = condition
		transactions["stock_symbol"] = stock_symbol
		transactions["num_shares"] = num_shares
		transactions["stock_price_realtime"] = float(stock_price_realtime)
		
		# amount buying stocks spent
		stock_amount_spent = num_shares * stock_price_realtime
		self.update_customer_balance(customer_id, stock_amount_spent, condition)

		return "Transaction_Records", transactions

	def update_customer_balance(self, customer_id : int, stock_amount_spent : float, condition : str):
		try:
			# get current balance from customer info
			api_url = self.url + "/rest/v1/" + "Customer_Information" + "?customer_id=eq." + str(customer_id)
			parameters =  {"apikey":self.keys}
			customer_data = requests.get(url = api_url, params = parameters)
			current_balance = customer_data.json()[0]['account_balance']

			# update balance and check condition
			if (condition == "buy"):
				update_balance = current_balance - stock_amount_spent
			elif (condition == "sell"):
				update_balance = current_balance + stock_amount_spent

			# update the customer account balance 
			data_to_insert = {"account_balance" : update_balance}
			response = requests.patch(url = api_url, params = parameters, json = data_to_insert)
		except:
			print("Fail to update customer balance")

	def supabase_insert_function(self, table_name : str, data_to_insert : dict)->str:
		"""
		excute rest api command to insert data to supabase 
		"""
		try:
			# route to table
			api_url = self.url + "/rest/v1/" + table_name

			parameters =  {"apikey":self.keys}

			response = requests.post(url = api_url, params = parameters, json = data_to_insert)
	
		except:
			print("Fail to implement supabse insert function")

# buy and sell stocks at realtime 
class Buy_And_Sell(object):
	def __init__(self, STOCK_API_KEYS):
		self.keys = STOCK_API_KEYS

	def get_realtime_stock_price(self, stock_symbol : str):
		# real time data get from 1 day period and interval 1 minute
		print(stock_symbol)
		data = yf.download(tickers= stock_symbol, period='1d', interval='1m')

		return float(data.iloc[-1]["Adj Close"])
	# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=1min&apikey=demo
	def realtime_price_bkp(self, stock_symbol : str):
		# example symbol : "AAPL" or "IBM"
		base_url = 'https://www.alphavantage.co/query?'
		params = {"function": "TIME_SERIES_INTRADAY", "symbol": stock_symbol, "interval": "1min", "apikey": self.keys}
		response = requests.get(base_url, params=params)
		data = response.json() # dict

		count_one = 0
		print(data)
		stock_price = 0
		for k,v in data["Time Series (1min)"].items():
			if (count_one == 1):
				break
			stock_price = v["4. close"]

			count_one = count_one + 1

		return stock_price

# stock information and stock data goes here 
class Stock_Data(object):
	def __init__(self, SUPABASE_URL, KEYS, STOCK_API_KEYS):
		self.url = SUPABASE_URL
		self.db_keys = KEYS		
		self.stock_keys = STOCK_API_KEYS

	# check and update stock symbol 5 years price data here
	def get_stock_information(self, stock_symbol : str):
		base_url = 'https://www.alphavantage.co/query?'
		params = {"function": "OVERVIEW", "symbol": stock_symbol, "apikey": self.stock_keys}
		response = requests.get(base_url, params=params)
		data = response.json() # dict

		# "stock_symbol", "stock_full_name", "exchange", "sector", "industry"	

		print(data)


# get / view data from database
class Table_View(object):
	def __init__(self, SUPABASE_URL, KEYS):
		self.url = SUPABASE_URL
		self.keys = KEYS


	pass


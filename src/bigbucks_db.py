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

TABLE_NAME = ["Customer_Information", "Customer_Password", "Stock_Name", "Stock_Price_Daily_Data", "Transaction_Records"]

# Customer_Information = ["customer_id", "first_name", "last_name", "phone_number", "email_address", "user_name", "password", "created_at"]
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
	def update_stock_name(self, stock_symbol : str, stock_full_name : str, exchange : str, sector : str, industry : str):
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
	def update_transaction_records(self, user_name : str, stock_symbol : str, num_shares : int, stock_price_realtime : float):
		# user_name is required to get the customer id
		customer_id = self.get_customer_id("Customer_Information", user_name)

		transactions = {}
		transactions["customer_id"] = customer_id
		transactions["stock_symbol"] = stock_symbol
		transactions["num_shares"] = num_shares
		transactions["stock_price_realtime"] = stock_price_realtime

		return "Transaction_Records", transactions

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









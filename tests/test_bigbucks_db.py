import sys
sys.path.append('../src') 

import bigbucks_db as bk

STOCK_API_KEYS = "9Q91BWGMOE13WOR3"
# Enter database url and keys here
SUPABASE_URL = ""
KEYS = ""

# db = bk.Table_Updates(SUPABASE_URL, KEYS, STOCK_API_KEYS)

# objs = bk.Buy_And_Sell("9Q91BWGMOE13WOR3")
# price = objs.get_realtime_stock_price("IBM")
# print(price)

# test = db.update_transaction_records("Jeffd", "buy", "IBM", 100, price)
# print(test)

# connect = db.supabase_insert_function(test[0], test[1])

import time
start_time = time.time()
#ob2 = bk.Stock_Data(SUPABASE_URL, KEYS, STOCK_API_KEYS)
# data = ob2.get_stock_information("IBM")
# ob2.update_stock_info(data)

# data2 = ob2.update_all_stock_price()
# print(data2)
# print(ob2.check_symbol_exist("AAPL"))

data3 = bk.Table_View(SUPABASE_URL,KEYS)
d3 = data3.view_customer_portfolio("Jeffd")
print(d3)
# data4 = bk.SP500(SUPABASE_URL, KEYS, STOCK_API_KEYS)
# d4 = data4.realtime_sp500()
# print(d4)
# test = bk.Buy_And_Sell(STOCK_API_KEYS)
# print(test.realtime_price_bkp("MSFT"))

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.2f} seconds")





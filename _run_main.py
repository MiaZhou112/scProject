from Main.main import *
from Main.utils import read_config
import yaml

cfg = read_config('config.yaml')

orders = get_data(cfg["MAIN_DATA"])
prices = get_unitPrices(cfg["ADD_DATA"])
check_missings(orders)
check_duplicates(orders)
df = merge_orders_and_prices_data(orders,prices)
df1 = add_salesAmount_month_column(df)
monthly_sales(df1)
delivery_performance(df1)

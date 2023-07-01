import pandas as pd
import openpyxl
import yaml
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


def get_data(data1):
    orders = pd.read_excel(data1,index_col=None)
    print(orders.head())
    return orders

def get_unitPrices(data2):
    prices = pd.read_excel(data2,index_col=None)
    print(prices.head())
    return prices

def check_missings(data1):
    number_of_missing = str(data1.isnull().sum().sum())
    print(f"number_of_missing is {number_of_missing}")

def check_duplicates(data1):
    number_of_duplicated_rows = data1.duplicated()
    if "True" in number_of_duplicated_rows:
        duplicates_counts = number_of_duplicated_rows.value_counts()['True']
        print(f"number of duplicated rows is {duplicates_counts}")
    else:
        print("no duplicated rows found")

def merge_orders_and_prices_data(data1,data2):
    df = pd.merge(data1,data2,on ="Product ID", how="left")
    print(df.head())
    return df

def add_salesAmount_month_column(df1):
    df1['Sales Amount(billion)'] = round(df1['Unit_Price'] * df1['Unit quantity'] / 1000000,2)
    df1['Month'] = pd.to_datetime(df1['Order Date']).dt.month
    print(df1.head())
    print(df1.columns)
    return df1

def monthly_sales(df1):
    agg = df1['Sales Amount(billion)'].groupby(df1['Month']).sum()
    print(agg)
    ax = agg.plot(kind = 'line',color = 'green',)
    ax.set_title('Monthly Sales in 2022',fontsize = 16)
    ax.set_xlabel('Month')
    ax.set_ylabel('Sale Amount(billion)')
    plt.show()
    plt.savefig('Monthly Sales')

def delivery_performance(df1):
    bins = [-1,0,2,4,10]
    names = ['just on time', 'a bit late','late','very late']
    df1['Category'] = pd.cut(df1['Ship Late Day count'], bins= bins,labels= names)
    category_count = df1['Category'].value_counts()/len(df1)
    delivery_performance_data = {'category':category_count.index,'percentage':category_count.values}
    delivery_performance_df = pd.DataFrame(delivery_performance_data,columns=['category','percentage'],index=None)
    print(delivery_performance_df)
    ax1 = delivery_performance_df.plot(kind='bar', x= 'category',y='percentage', rot=0)
    ax1.set_title('Delivery Performance per Category',fontsize = 16)
    ax1.set_xlabel('Category')
    ax1.set_ylabel('Percentage')
    for i, v in enumerate(delivery_performance_df['percentage']):
        ax1.text(i, v, f'{v:.2%}', ha='center', va = 'baseline')
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=0))
    plt.show()
    plt.savefig('Delivery Performance per Category')


    







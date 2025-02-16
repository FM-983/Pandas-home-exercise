import pandas as pd
import numpy as np

products_df = pd.DataFrame({
    'Product_ID': [1, 2, 3],
    'Product_Name': ['iPhone 12', 'Samsung S21', 'Pixel 5'],
    'Product_Price': [999, 899, 699],
})


sales_df = pd.DataFrame({
    'Sale_ID': [1, 2, 3, 4, 5, 6, 7],
    'Sale_Date': pd.to_datetime(['2021-01-01', '2021-02-01', '2021-02-15','2020-03-01', '2020-04-01','2020-02-15', '2020-01-01']),
    'Customer_ID': [1, 2, 3, 2, 3, 4, 4],
    'Product_ID': [1, 1, 2, 2, 3, 3, 1],
})
customers_df = pd.DataFrame({
    'Customer_ID': [1, 2, 3, 4],
    'Customer_Name': ['John Doe', 'Jane Doe', 'Jim Brown', 'Jake Smith'],
    'Customer_Age': [25, 30, 35, 20],
    'Customer_Email': ['john@doe.com', 'jane@doe.com', 'jim@brown.com','jake@smith.com'],
})

"""
2)  Having the products_df and sales_df, merge both dataframes using
'Product_ID' as the key. Once you have it, display only the Sale_ID,
Product_Name and Product_Price columns.
"""
##
print(f"\n2) EXERCISE\n")
merge_df = pd.merge(products_df,sales_df, on= "Product_ID" , how= "inner")
print(merge_df[["Sale_ID","Product_Name","Product_Price"]])

"""
3) Add the following additional dataframes:
"""

apple_products_df = pd.DataFrame({
    'Product_ID': [4, 5],
    'Product_Name': ['iPhone 13', 'Apple Watch Series 6'],
    'Product_Price': [999, 399],
})

samsung_products_df = pd.DataFrame({
    'Product_ID': [6, 7],
    'Product_Name': ['Samsung S22', 'Galaxy Watch 4'],
    'Product_Price': [999, 250],
})

"""
Concatenate these dataframes with the original products_df and show the
final dataframe. Use a copy() and don’t change the original products_df.
"""

print(f"\n3) EXERCISE\n")
concat_df =  pd.concat([products_df,apple_products_df,samsung_products_df],axis=0).copy()
print(concat_df)

"""
4) With the resulting df from Exercise 1, group it by Product_Name and calculate
the total Product_Price.
"""
print(f"\n4) EXERCISE\n")
all_products_df = pd.concat([products_df.copy(), apple_products_df, samsung_products_df], ignore_index=True)
grouped_products = all_products_df.groupby('Product_Name')['Product_Price'].sum()
print(grouped_products)
"""
5) In the customers_df dataframe, set 'Customer_ID' and 'Customer_Email' as
indexes (multi indexing).
After that, display all the customers whose ID is less than 3.
"""
print(f"\n5) EXERCISE\n")

customers_df = customers_df.set_index(['Customer_ID', 'Customer_Email'])
print(customers_df)
customers_less_than_3 = customers_df.loc[customers_df.index.get_level_values('Customer_ID') < 3]
print(customers_less_than_3)

"""
6) Use merge, groupby, and other necessary functions to answer these
questions:
    a. Which customer(s) bought the most expensive product?
    b. On which date did we get the highest number of sales?
    c. What is the average price of the products purchased by each
    customer?
Remember to use multi-indexing, groupby, and date-time concepts wherever
necessary.
"""

print(f"\n6) EXERCISE A)\n")
most_expensive_product_price = products_df['Product_Price'].max()
most_expensive_product_name = products_df.loc[products_df['Product_Price'] == most_expensive_product_price, 'Product_Name'].iloc[0]

customers_most_expensive = pd.merge(merge_df, customers_df.reset_index(), on='Customer_ID')
customers_most_expensive = customers_most_expensive[customers_most_expensive['Product_Name'] == most_expensive_product_name]
print(f"Customer(s) who bought the most expensive product ({most_expensive_product_name}):")
print(customers_most_expensive['Customer_Name'].unique())

print(f"\n6) EXERCISE B)\n")
sales_count_by_date = sales_df.groupby('Sale_Date')['Sale_ID'].count()
highest_sales_date = sales_count_by_date.idxmax()
print(f"Date with the highest number of sales: {highest_sales_date}")

print(f"\n6) EXERCISE C)\n")

average_price_by_customer = merge_df.groupby('Customer_ID')['Product_Price'].mean()
print(f"Average price of products purchased by each customer:\n{average_price_by_customer}")
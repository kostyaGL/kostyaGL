# /*
# Table: Products
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | new_price     | int     |
# | change_date   | date    |
# +---------------+---------+
# (product_id, change_date) is the primary key (combination of columns with unique values) of this table.
# Each row of this table indicates that the price of some product was changed to a new price at some date.
#
#
# Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.
#
# Return the result table in any order.
#
# The result format is in the following example.
#
#
#
# Example 1:
#
# Input:
# Products table:
# +------------+-----------+-------------+
# | product_id | new_price | change_date |
# +------------+-----------+-------------+
# | 1          | 20        | 2019-08-14  |
# | 2          | 50        | 2019-08-14  |
# | 1          | 30        | 2019-08-15  |
# | 1          | 35        | 2019-08-16  |
# | 2          | 65        | 2019-08-17  |
# | 3          | 20        | 2019-08-18  |
# +------------+-----------+-------------+
# Output:
# +------------+-------+
# | product_id | price |
# +------------+-------+
# | 2          | 50    |
# | 1          | 35    |
# | 3          | 10    |
# +------------+-------+
# */
import pandas as pd

# Simulating the Products table as a pandas DataFrame
data = {
    'product_id': [1, 2, 1, 1, 2, 3],
    'new_price': [20, 50, 30, 35, 65, 20],
    'change_date': ['2019-08-14', '2019-08-14', '2019-08-15', '2019-08-16', '2019-08-17', '2019-08-18']
}

products_df = pd.DataFrame(data)

# Convert change_date to datetime format
products_df['change_date'] = pd.to_datetime(products_df['change_date'])

# Filter products that have a change_date on or before '2019-08-16'
filtered_products = products_df[products_df['change_date'] <= '2019-08-16']

# Find the latest price for each product
latest_prices = filtered_products.sort_values(by='change_date', ascending=False).drop_duplicates('product_id')

# Create a DataFrame with default price 10 for all products
all_products = pd.DataFrame({'product_id': products_df['product_id'].unique(), 'price': 10})

# Merge to get the final prices
result_df = pd.merge(all_products, latest_prices[['product_id', 'new_price']], on='product_id', how='left')

# Replace NaN (products without any price change) with default price 10
result_df['price'] = result_df['price'].fillna(10)

# Display the result
print(result_df)


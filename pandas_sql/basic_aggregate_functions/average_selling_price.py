# /*
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | start_date    | date    |
# | end_date      | date    |
# | price         | int     |
# +---------------+---------+
# (product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
# Each row of this table indicates the price of the product_id in the period from start_date to end_date.
# For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.
#
#
# Table: UnitsSold
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | purchase_date | date    |
# | units         | int     |
# +---------------+---------+
# This table may contain duplicate rows.
# Each row of this table indicates the date, units, and product_id of each product sold.
#
#
# Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places.
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
# Prices table:
# +------------+------------+------------+--------+
# | product_id | start_date | end_date   | price  |
# +------------+------------+------------+--------+
# | 1          | 2019-02-17 | 2019-02-28 | 5      |
# | 1          | 2019-03-01 | 2019-03-22 | 20     |
# | 2          | 2019-02-01 | 2019-02-20 | 15     |
# | 2          | 2019-02-21 | 2019-03-31 | 30     |
# +------------+------------+------------+--------+
# UnitsSold table:
# +------------+---------------+-------+
# | product_id | purchase_date | units |
# +------------+---------------+-------+
# | 1          | 2019-02-25    | 100   |
# | 1          | 2019-03-01    | 15    |
# | 2          | 2019-02-10    | 200   |
# | 2          | 2019-03-22    | 30    |
# +------------+---------------+-------+
# Output:
# +------------+---------------+
# | product_id | average_price |
# +------------+---------------+
# | 1          | 6.96          |
# | 2          | 16.96         |
# +------------+---------------+
# Explanation:
# Average selling price = Total Price of Product / Number of products sold.
# Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96
# Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96
# */
#
# WITH Prices AS (
#     SELECT 1 AS product_id, '2019-02-17' AS start_date, '2019-02-28' AS end_date, 5 AS price UNION ALL
#     SELECT 1 AS product_id, '2019-03-01' AS start_date, '2019-03-22' AS end_date, 20 AS price UNION ALL
#     SELECT 2 AS product_id, '2019-02-01' AS start_date, '2019-02-20' AS end_date, 15 AS price UNION ALL
#     SELECT 2 AS product_id, '2019-02-21' AS start_date, '2019-03-31' AS end_date, 30 AS price
# ),
# UnitsSold AS (
#     SELECT 1 AS product_id, '2019-02-25' AS purchase_date, 100 AS units UNION ALL
#     SELECT 1 AS product_id, '2019-03-01' AS purchase_date, 15 AS units UNION ALL
#     SELECT 2 AS product_id, '2019-02-10' AS purchase_date, 200 AS units UNION ALL
#     SELECT 2 AS product_id, '2019-03-22' AS purchase_date, 30 AS units
# ),
# Sales AS (
#     SELECT
#         u.product_id,
#         u.purchase_date,
#         u.units,
#         p.price
#     FROM
#         UnitsSold u
#     JOIN
#         Prices p
#     ON
#         u.product_id = p.product_id
#         AND u.purchase_date BETWEEN p.start_date AND p.end_date
# )
# SELECT
#     product_id,
#     SUM(units * price) / SUM(units) AS total_revenue
# FROM
#     Sales
# GROUP BY
#     product_id;
import pandas as pd

# Sample data (you can replace this with your SQL query or actual data source)
prices_data = {
    'product_id': [1, 1, 2, 2],
    'start_date': ['2019-02-17', '2019-03-01', '2019-02-01', '2019-02-21'],
    'end_date': ['2019-02-28', '2019-03-22', '2019-02-20', '2019-03-31'],
    'price': [5, 20, 15, 30]
}

units_sold_data = {
    'product_id': [1, 1, 2, 2],
    'purchase_date': ['2019-02-25', '2019-03-01', '2019-02-10', '2019-03-22'],
    'units': [100, 15, 200, 30]
}

# Convert sample data to pandas DataFrames
prices_df = pd.DataFrame(prices_data)
units_sold_df = pd.DataFrame(units_sold_data)

# Merge or join prices and units_sold on product_id and purchase_date falling within start_date and end_date
merged_df = pd.merge(units_sold_df, prices_df, on='product_id')
merged_df = merged_df[(merged_df['purchase_date'] >= merged_df['start_date']) & (merged_df['purchase_date'] <= merged_df['end_date'])]

# Calculate total revenue
merged_df['total_revenue'] = merged_df['units'] * merged_df['price']

# Calculate average price rounded to 2 decimal places
average_price_df = merged_df.groupby('product_id')['total_revenue', 'units'].sum()
average_price_df['average_price'] = (average_price_df['total_revenue'] / average_price_df['units']).round(2)

# Display the result
result_df = average_price_df[['average_price']].reset_index()
print(result_df)

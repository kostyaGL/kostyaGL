# /*
# Table: Products
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | product_id       | int     |
# | product_name     | varchar |
# | product_category | varchar |
# +------------------+---------+
# product_id is the primary key (column with unique values) for this table.
# This table contains data about the company's products.
#
#
# Table: Orders
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | order_date    | date    |
# | unit          | int     |
# +---------------+---------+
# This table may have duplicate rows.
# product_id is a foreign key (reference column) to the Products table.
# unit is the number of products ordered in order_date.
#
#
# Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount.
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
# +-------------+-----------------------+------------------+
# | product_id  | product_name          | product_category |
# +-------------+-----------------------+------------------+
# | 1           | Leetcode Solutions    | Book             |
# | 2           | Jewels of Stringology | Book             |
# | 3           | HP                    | Laptop           |
# | 4           | Lenovo                | Laptop           |
# | 5           | Leetcode Kit          | T-shirt          |
# +-------------+-----------------------+------------------+
# Orders table:
# +--------------+--------------+----------+
# | product_id   | order_date   | unit     |
# +--------------+--------------+----------+
# | 1            | 2020-02-05   | 60       |
# | 1            | 2020-02-10   | 70       |
# | 2            | 2020-01-18   | 30       |
# | 2            | 2020-02-11   | 80       |
# | 3            | 2020-02-17   | 2        |
# | 3            | 2020-02-24   | 3        |
# | 4            | 2020-03-01   | 20       |
# | 4            | 2020-03-04   | 30       |
# | 4            | 2020-03-04   | 60       |
# | 5            | 2020-02-25   | 50       |
# | 5            | 2020-02-27   | 50       |
# | 5            | 2020-03-01   | 50       |
# +--------------+--------------+----------+
# Output:
# +--------------------+---------+
# | product_name       | unit    |
# +--------------------+---------+
# | Leetcode Solutions | 130     |
# | Leetcode Kit       | 100     |
# +--------------------+---------+
# Explanation:
# Products with product_id = 1 is ordered in February a total of (60 + 70) = 130.
# Products with product_id = 2 is ordered in February a total of 80.
# Products with product_id = 3 is ordered in February a total of (2 + 3) = 5.
# Products with product_id = 4 was not ordered in February 2020.
# Products with product_id = 5 is ordered in February a total of (50 + 50) = 100.
#
# */
#
# WITH Products AS (
#     SELECT 1 AS product_id, 'Leetcode Solutions' AS product_name, 'Book' AS product_category
#     UNION ALL
#     SELECT 2, 'Jewels of Stringology', 'Book'
#     UNION ALL
#     SELECT 3, 'HP', 'Laptop'
#     UNION ALL
#     SELECT 4, 'Lenovo', 'Laptop'
#     UNION ALL
#     SELECT 5, 'Leetcode Kit', 'T-shirt'
# ),
# Orders AS (
#     SELECT 1 AS product_id, '2020-02-05' AS order_date, 60 AS unit
#     UNION ALL
#     SELECT 1, '2020-02-10', 70
#     UNION ALL
#     SELECT 2, '2020-01-18', 30
#     UNION ALL
#     SELECT 2, '2020-02-11', 80
#     UNION ALL
#     SELECT 3, '2020-02-17', 2
#     UNION ALL
#     SELECT 3, '2020-02-24', 3
#     UNION ALL
#     SELECT 4, '2020-03-01', 20
#     UNION ALL
#     SELECT 4, '2020-03-04', 30
#     UNION ALL
#     SELECT 4, '2020-03-04', 60
#     UNION ALL
#     SELECT 5, '2020-02-25', 50
#     UNION ALL
#     SELECT 5, '2020-02-27', 50
#     UNION ALL
#     SELECT 5, '2020-03-01', 50
# )
# SELECT
#     p.product_name,
#     SUM(o.unit) unit
# FROM
#     Orders o
# JOIN
#     Products p ON p.product_id=o.product_id
# WHERE
#     DATE_TRUNC(PARSE_DATE('%Y-%m-%d', o.order_date), MONTH) = '2020-02-01'
# GROUP BY
#     o.product_id,
#     p.product_name,
#     DATE_TRUNC(PARSE_DATE('%Y-%m-%d', o.order_date), MONTH)
# HAVING unit >= 100
import pandas as pd

# Sample data as defined in the SQL query
products_data = {
    'product_id': [1, 2, 3, 4, 5],
    'product_name': ['Leetcode Solutions', 'Jewels of Stringology', 'HP', 'Lenovo', 'Leetcode Kit'],
    'product_category': ['Book', 'Book', 'Laptop', 'Laptop', 'T-shirt']
}

orders_data = {
    'product_id': [1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5],
    'order_date': ['2020-02-05', '2020-02-10', '2020-01-18', '2020-02-11', '2020-02-17', '2020-02-24',
                   '2020-03-01', '2020-03-04', '2020-03-04', '2020-02-25', '2020-02-27', '2020-03-01'],
    'unit': [60, 70, 30, 80, 2, 3, 20, 30, 60, 50, 50, 50]
}

# Create pandas DataFrames from the sample data
products_df = pd.DataFrame(products_data)
orders_df = pd.DataFrame(orders_data)

# Convert order_date to datetime type
orders_df['order_date'] = pd.to_datetime(orders_df['order_date'])

# Filter orders for February 2020
orders_feb_df = orders_df[(orders_df['order_date'].dt.year == 2020) & (orders_df['order_date'].dt.month == 2)]

# Group by product_id to sum units sold
grouped_orders = orders_feb_df.groupby('product_id')['unit'].sum().reset_index()

# Merge with products_df to get product names
merged_df = pd.merge(grouped_orders, products_df, on='product_id', how='inner')

# Filter products with at least 100 units sold
filtered_df = merged_df[merged_df['unit'] >= 100]

# Prepare final result DataFrame
result_df = filtered_df[['product_name', 'unit']].sort_values(by='product_name').reset_index(drop=True)

# Display the result
print(result_df)

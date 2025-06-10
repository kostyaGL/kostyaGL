"""

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.


Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.


Write a solution to report the product_name, year, and price for each sale_id in the Sales table.

Return the resulting table in any order.

The result format is in the following example.



Example 1:

Input:
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
Output:
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Nokia        | 2008  | 5000  |
| Nokia        | 2009  | 5000  |
| Apple        | 2011  | 9000  |
+--------------+-------+-------+
Explanation:
From sale_id = 1, we can conclude that Nokia was sold for 5000 in the year 2008.
From sale_id = 2, we can conclude that Nokia was sold for 5000 in the year 2009.
From sale_id = 7, we can conclude that Apple was sold for 9000 in the year 2011.
*/
-- Using CTE to define the Sales and Product tables
WITH Sales AS (
  SELECT 1 AS sale_id, 100 AS product_id, 2008 AS year, 10 AS quantity, 5000 AS price UNION ALL
  SELECT 2, 100, 2009, 12, 5000 UNION ALL
  SELECT 7, 200, 2011, 15, 9000
),
Product AS (
  SELECT 100 AS product_id, 'Nokia' AS product_name UNION ALL
  SELECT 200, 'Apple' UNION ALL
  SELECT 300, 'Samsung'
)

-- Join the CTEs to get the desired result
SELECT s.sale_id, s.product_id, p.product_name, s.year, s.quantity, s.price
FROM Sales s
JOIN Product p
ON s.product_id = p.product_id;
"""
import pandas as pd

# Sample data for Sales table
sales_data = {
    'sale_id': [1, 2, 7],
    'product_id': [100, 100, 200],
    'year': [2008, 2009, 2011],
    'quantity': [10, 12, 15],
    'price': [5000, 5000, 9000]
}

# Sample data for Product table
product_data = {
    'product_id': [100, 200, 300],
    'product_name': ['Nokia', 'Apple', 'Samsung']
}

# Convert data to pandas DataFrames
df_sales = pd.DataFrame(sales_data)
df_product = pd.DataFrame(product_data)

# Perform join to combine Sales and Product tables
df_result = pd.merge(df_sales, df_product, on='product_id')

# Select and reorder the columns to match the desired output
df_final = df_result[['product_name', 'year', 'price']]

# Display the final DataFrame
print(df_final)

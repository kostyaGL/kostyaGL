"""/*
Table: Sales

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


Write a solution to select the product id, year, quantity, and price for the first year of every product sold.

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
+------------+------------+----------+-------+
| product_id | first_year | quantity | price |
+------------+------------+----------+-------+
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |
+------------+------------+----------+-------+
*/

WITH Sales AS (
    SELECT 1 AS sale_id, 100 AS product_id, 2008 AS year, 10 AS quantity, 5000 AS price UNION ALL
    SELECT 2 AS sale_id, 100 AS product_id, 2009 AS year, 12 AS quantity, 5000 AS price UNION ALL
    SELECT 7 AS sale_id, 200 AS product_id, 2011 AS year, 15 AS quantity, 9000 AS price
),
Product AS (
    SELECT 100 AS product_id, 'Nokia' AS product_name UNION ALL
    SELECT 200 AS product_id, 'Apple' AS product_name UNION ALL
    SELECT 300 AS product_id, 'Samsung' AS product_name
)
SELECT
 s.product_id,
 s.year,
 s.quantity,
 s.price
FROM Sales s
JOIN Product p ON s.product_id=p.product_id
JOIN (select product_id as product_id, min(year) year from Sales GROUP BY product_id) p1 ON s.product_id=p1.product_id and s.year=p1.year
"""

import pandas as pd

# Simulating the Sales table
sales_data = {
    'sale_id': [1, 2, 7],
    'product_id': [100, 100, 200],
    'year': [2008, 2009, 2011],
    'quantity': [10, 12, 15],
    'price': [5000, 5000, 9000]
}

sales = pd.DataFrame(sales_data)

# Simulating the Product table
product_data = {
    'product_id': [100, 200, 300],
    'product_name': ['Nokia', 'Apple', 'Samsung']
}

products = pd.DataFrame(product_data)

# Finding the first year each product was sold
first_year_sales = sales.groupby('product_id')['year'].min().reset_index()

# Joining to get the desired output
result = pd.merge(first_year_sales, sales, on=['product_id', 'year'])

# Selecting the required columns
result = result[['product_id', 'year', 'quantity', 'price']]

print(result)

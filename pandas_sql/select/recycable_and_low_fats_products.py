"""
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.


Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Output:
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation: Only products 1 and 3 are both low fat and recyclable.
 */

WITH products_cte AS (
  SELECT 0 AS product_id, 'Y' AS low_fats, 'N' AS recyclable UNION ALL
  SELECT 1, 'Y', 'Y' UNION ALL
  SELECT 2, 'N', 'Y' UNION ALL
  SELECT 3, 'Y', 'Y' UNION ALL
  SELECT 4, 'N', 'N'
)

SELECT
  *
FROM
  products_cte
WHERE
  low_fats = 'Y'
  AND recyclable = 'Y';
"""

import pandas as pd

# Sample data for Products table
products_data = {
    'product_id': [0, 1, 2, 3, 4],
    'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
    'recyclable': ['N', 'Y', 'Y', 'Y', 'N']
}

# Convert data to pandas DataFrame
df_products = pd.DataFrame(products_data)

# Filter the DataFrame to include only products that are both low fat and recyclable
df_filtered = df_products[(df_products['low_fats'] == 'Y') & (df_products['recyclable'] == 'Y')]

# Select the required column
df_result = df_filtered[['product_id']]

# Display the final DataFrame
print(df_result)

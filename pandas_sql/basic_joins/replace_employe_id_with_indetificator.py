"""

Table: Employees

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.


Table: EmployeeUNI

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the company.


Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Employees table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+
EmployeeUNI table:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
Output:
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
Explanation:
Alice and Bob do not have a unique ID, We will show null instead.
The unique ID of Meir is 2.
The unique ID of Winston is 3.
The unique ID of Jonathan is 1.
*/

-- Using CTE to define the Employees and EmployeeUNI tables
WITH Employees AS (
  SELECT 1 AS id, 'Alice' AS name UNION ALL
  SELECT 7, 'Bob' UNION ALL
  SELECT 11, 'Meir' UNION ALL
  SELECT 90, 'Winston' UNION ALL
  SELECT 3, 'Jonathan'
),
EmployeeUNI AS (
  SELECT 3 AS id, 1 AS unique_id UNION ALL
  SELECT 11, 2 UNION ALL
  SELECT 90, 3
)

-- Join the CTEs to get the desired result
SELECT u.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI u
ON e.id = u.id
"""

import pandas as pd

# Sample data for Employees table
employees_data = {
    'id': [1, 7, 11, 90, 3],
    'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']
}

# Sample data for EmployeeUNI table
employeeuni_data = {
    'id': [3, 11, 90],
    'unique_id': [1, 2, 3]
}

# Convert data to pandas DataFrames
df_employees = pd.DataFrame(employees_data)
df_employeeuni = pd.DataFrame(employeeuni_data)

# Perform left join to combine Employees and EmployeeUNI tables
df_result = pd.merge(df_employees, df_employeeuni, on='id', how='left')

# Select and reorder the columns to match the desired output
df_final = df_result[['unique_id', 'name']]

# Display the final DataFrame
print(df_final)

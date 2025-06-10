"""
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| empId       | int     |
| name        | varchar |
| supervisor  | int     |
| salary      | int     |
+-------------+---------+
empId is the column with unique values for this table.
Each row of this table indicates the name and the ID of an employee in addition to their salary and the id of their manager.


Table: Bonus

+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+
empId is the column of unique values for this table.
empId is a foreign key (reference column) to empId from the Employee table.
Each row of this table contains the id of an employee and their respective bonus.


Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Employee table:
+-------+--------+------------+--------+
| empId | name   | supervisor | salary |
+-------+--------+------------+--------+
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |
+-------+--------+------------+--------+
Bonus table:
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
Output:
+------+-------+
| name | bonus |
+------+-------+
| Brad | null  |
| John | null  |
| Dan  | 500   |
+------+-------+
*/

WITH Employee AS (
  SELECT 3 AS empId, 'Brad' AS name, NULL AS supervisor, 4000 AS salary UNION ALL
  SELECT 1 AS empId, 'John' AS name, 3 AS supervisor, 1000 AS salary UNION ALL
  SELECT 2 AS empId, 'Dan' AS name, 3 AS supervisor, 2000 AS salary UNION ALL
  SELECT 4 AS empId, 'Thomas' AS name, 3 AS supervisor, 4000 AS salary
),
Bonus AS (
  SELECT 2 AS empId, 500 AS bonus UNION ALL
  SELECT 4 AS empId, 2000 AS bonus
)

-- Query to combine Employee and Bonus tables
SELECT
  e.name,
  b.bonus
FROM
  Employee e
LEFT JOIN
  Bonus b
ON
  e.empId = b.empId
WHERE b.bonus is null OR b.bonus <= 500;

"""
import pandas as pd

# Sample data as Python dictionaries
employee_data = [
    {'empId': 3, 'name': 'Brad', 'supervisor': None, 'salary': 4000},
    {'empId': 1, 'name': 'John', 'supervisor': 3, 'salary': 1000},
    {'empId': 2, 'name': 'Dan', 'supervisor': 3, 'salary': 2000},
    {'empId': 4, 'name': 'Thomas', 'supervisor': 3, 'salary': 4000}
]

bonus_data = [
    {'empId': 2, 'bonus': 500},
    {'empId': 4, 'bonus': 2000}
]

# Convert data to pandas DataFrames
df_employee = pd.DataFrame(employee_data)
df_bonus = pd.DataFrame(bonus_data)

# Perform left join to combine Employee and Bonus tables
df_result = pd.merge(df_employee, df_bonus, on='empId', how='left')

# Filter and modify the DataFrame to match the SQL WHERE condition
df_result['bonus'] = df_result['bonus'].where(df_result['bonus'].isnull() | (df_result['bonus'] <= 500), None)

# Select columns 'name' and 'bonus'
df_final = df_result[['name', 'bonus']]

# Display the final DataFrame
print(df_final)

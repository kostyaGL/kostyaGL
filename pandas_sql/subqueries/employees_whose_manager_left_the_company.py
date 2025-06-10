"""/*
Table: Employees

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| manager_id  | int      |
| salary      | int      |
+-------------+----------+
In SQL, employee_id is the primary key for this table.
This table contains information about the employees, their salary, and the ID of their manager. Some employees do not have a manager (manager_id is null).


Find the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.

Return the result table ordered by employee_id.

The result format is in the following example.



Example 1:

Input:
Employees table:
+-------------+-----------+------------+--------+
| employee_id | name      | manager_id | salary |
+-------------+-----------+------------+--------+
| 3           | Mila      | 9          | 60301  |
| 12          | Antonella | null       | 31000  |
| 13          | Emery     | null       | 67084  |
| 1           | Kalel     | 11         | 21241  |
| 9           | Mikaela   | null       | 50937  |
| 11          | Joziah    | 6          | 28485  |
+-------------+-----------+------------+--------+
Output:
+-------------+
| employee_id |
+-------------+
| 11          |
+-------------+

Explanation:
The employees with a salary less than $30000 are 1 (Kalel) and 11 (Joziah).
Kalel's manager is employee 11, who is still in the company (Joziah).
Joziah's manager is employee 6, who left the company because there is no row for employee 6 as it was deleted.
*/
WITH Employees AS (
    SELECT 3 AS employee_id, 'Mila' AS name, 9 AS manager_id, 60301 AS salary UNION ALL
    SELECT 12 AS employee_id, 'Antonella' AS name, NULL AS manager_id, 31000 AS salary UNION ALL
    SELECT 13 AS employee_id, 'Emery' AS name, NULL AS manager_id, 67084 AS salary UNION ALL
    SELECT 1 AS employee_id, 'Kalel' AS name, 11 AS manager_id, 21241 AS salary UNION ALL
    SELECT 9 AS employee_id, 'Mikaela' AS name, NULL AS manager_id, 50937 AS salary UNION ALL
    SELECT 11 AS employee_id, 'Joziah' AS name, 6 AS manager_id, 28485 AS salary
)
SELECT
    employee_id
FROM Employees where manager_id not in (select employee_id from Employees) and salary < 30000
"""

import pandas as pd

# Simulate the Employees table
data = {
    'employee_id': [3, 12, 13, 1, 9, 11],
    'name': ['Mila', 'Antonella', 'Emery', 'Kalel', 'Mikaela', 'Joziah'],
    'manager_id': [9, None, None, 11, None, 6],
    'salary': [60301, 31000, 67084, 21241, 50937, 28485]
}

# Create DataFrame
df = pd.DataFrame(data)

# Filter employees with salary less than 30000 and manager_id not in employee_id
result_df = df[(df['salary'] < 30000) & (~df['manager_id'].isin(df['employee_id'].tolist()))]

# Extract the employee_id column as output
output = result_df['employee_id'].tolist()

print(output)

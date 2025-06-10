"""

Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.


Write a solution to find managers with at least five direct reports.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output:
+------+
| name |
+------+
| John |
+------+
*/

WITH Employee AS (
  SELECT 101 AS id, 'John' AS name, 'A' AS department, NULL AS managerId UNION ALL
  SELECT 102 AS id, 'Dan' AS name, 'A' AS department, 101 AS managerId UNION ALL
  SELECT 103 AS id, 'James' AS name, 'A' AS department, 101 AS managerId UNION ALL
  SELECT 104 AS id, 'Amy' AS name, 'A' AS department, 101 AS managerId UNION ALL
  SELECT 105 AS id, 'Anne' AS name, 'A' AS department, 101 AS managerId UNION ALL
  SELECT 106 AS id, 'Ron' AS name, 'B' AS department, 101 AS managerId
)

-- Example query to retrieve all data from the CTE
SELECT e1.name
FROM Employee e1
LEFT JOIN Employee e2 ON e1.id=e2.managerId
GROUP BY e1.name
HAVING COUNT(e2.name) >= 5;
"""

import pandas as pd

# Sample data as Python dictionaries
data = {
    'id': [101, 102, 103, 104, 105, 106],
    'name': ['John', 'Dan', 'James', 'Amy', 'Anne', 'Ron'],
    'department': ['A', 'A', 'A', 'A', 'A', 'B'],
    'managerId': [None, 101, 101, 101, 101, 101]
}

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Find the manager who manages at least 5 employees in the same department
manager_candidates = df[df['managerId'].isnull()]  # Filter for managers (managerId is null)
# Merge manager_candidates with itself on managerId
merged_df = pd.merge(manager_candidates, df, left_on='id', right_on='managerId', how='right', suffixes=('_manager', '_employee'))

# Group by manager name and count employees managed per department
grouped = merged_df.groupby(['name_manager']).size().reset_index(name='count_managed')

# Filter for managers who manage at least 5 employees in the same department
qualified_managers = grouped[(grouped['count_managed'] >= 5)]

# Display the names of qualified managers
print(qualified_managers['name_manager'].tolist())

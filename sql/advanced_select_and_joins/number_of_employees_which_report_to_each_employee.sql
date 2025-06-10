/*
Table: Employees

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| reports_to  | int      |
| age         | int      |
+-------------+----------+
employee_id is the column with unique values for this table.
This table contains information about the employees and the id of the manager they report to. Some employees do not report to anyone (reports_to is null).


For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them.

Write a solution to report the ids and the names of all managers, the number of employees who report directly to them, and the average age of the reports rounded to the nearest integer.

Return the result table ordered by employee_id.

The result format is in the following example.



Example 1:

Input:
Employees table:
+-------------+---------+------------+-----+
| employee_id | name    | reports_to | age |
+-------------+---------+------------+-----+
| 9           | Hercy   | null       | 43  |
| 6           | Alice   | 9          | 41  |
| 4           | Bob     | 9          | 36  |
| 2           | Winston | null       | 37  |
+-------------+---------+------------+-----+
Output:
+-------------+-------+---------------+-------------+
| employee_id | name  | reports_count | average_age |
+-------------+-------+---------------+-------------+
| 9           | Hercy | 2             | 39          |
+-------------+-------+---------------+-------------+
Explanation: Hercy has 2 people report directly to him, Alice and Bob. Their average age is (41+36)/2 = 38.5, which is 39 after rounding it to the nearest integer.
Example 2:

Input:
Employees table:
+-------------+---------+------------+-----+
| employee_id | name    | reports_to | age |
|-------------|---------|------------|-----|
| 1           | Michael | null       | 45  |
| 2           | Alice   | 1          | 38  |
| 3           | Bob     | 1          | 42  |
| 4           | Charlie | 2          | 34  |
| 5           | David   | 2          | 40  |
| 6           | Eve     | 3          | 37  |
| 7           | Frank   | null       | 50  |
| 8           | Grace   | null       | 48  |
+-------------+---------+------------+-----+
Output:
+-------------+---------+---------------+-------------+
| employee_id | name    | reports_count | average_age |
| ----------- | ------- | ------------- | ----------- |
| 1           | Michael | 2             | 40          |
| 2           | Alice   | 2             | 37          |
| 3           | Bob     | 1             | 37          |
+-------------+---------+---------------+-------------+
*/

WITH Employees AS (
    SELECT 1 AS employee_id, 'Michael' AS name, NULL AS reports_to, 45 AS age UNION ALL
    SELECT 2 AS employee_id, 'Alice' AS name, 1 AS reports_to, 38 AS age UNION ALL
    SELECT 3 AS employee_id, 'Bob' AS name, 1 AS reports_to, 42 AS age UNION ALL
    SELECT 4 AS employee_id, 'Charlie' AS name, 2 AS reports_to, 34 AS age UNION ALL
    SELECT 5 AS employee_id, 'David' AS name, 2 AS reports_to, 40 AS age UNION ALL
    SELECT 6 AS employee_id, 'Eve' AS name, 3 AS reports_to, 37 AS age UNION ALL
    SELECT 7 AS employee_id, 'Frank' AS name, NULL AS reports_to, 50 AS age UNION ALL
    SELECT 8 AS employee_id, 'Grace' AS name, NULL AS reports_to, 48 AS age
)
SELECT
    e.employee_id,
    e.name,
    CAST(CEIL(AVG(e1.age)) as INT) age
FROM
    Employees e
RIGHT JOIN Employees e1 ON e.employee_id=e1.reports_to
WHERE e.employee_id is not null
GROUP BY e.employee_id, e.name


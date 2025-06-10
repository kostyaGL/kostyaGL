"""/*
Table: Courses

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.


Write a solution to find all the classes that have at least five students.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+
Output:
+---------+
| class   |
+---------+
| Math    |
+---------+
Explanation:
- Math has 6 students, so we include it.
- English has 1 student, so we do not include it.
- Biology has 1 student, so we do not include it.
- Computer has 1 student, so we do not include it.
*/

WITH Courses AS (
    SELECT 'A' AS student, 'Math' AS class UNION ALL
    SELECT 'B' AS student, 'English' AS class UNION ALL
    SELECT 'C' AS student, 'Math' AS class UNION ALL
    SELECT 'D' AS student, 'Biology' AS class UNION ALL
    SELECT 'E' AS student, 'Math' AS class UNION ALL
    SELECT 'F' AS student, 'Computer' AS class UNION ALL
    SELECT 'G' AS student, 'Math' AS class UNION ALL
    SELECT 'H' AS student, 'Math' AS class UNION ALL
    SELECT 'I' AS student, 'Math' AS class
)
SELECT
    class
FROM
    Courses
GROUP BY class
HAVING count(*) >= 5
"""
import pandas as pd

# Sample data for Courses table
courses_data = {
    'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Computer', 'Math', 'Math', 'Math']
}

# Convert data to pandas DataFrame
df_courses = pd.DataFrame(courses_data)

# Group by the 'class' column and count the number of students in each class
class_counts = df_courses.groupby('class').size().reset_index(name='student_count')

# Filter classes that have 5 or more students
popular_classes = class_counts[class_counts['student_count'] >= 5]['class']

# Display the final DataFrame
result = pd.DataFrame({'class': popular_classes})
print(result)

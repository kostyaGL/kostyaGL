"""/*
Table: Teacher

+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+
(subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.
Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.


Write a solution to calculate the number of unique subjects each teacher teaches in the university.

Return the result table in any order.

The result format is shown in the following example.



Example 1:

Input:
Teacher table:
+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |
+------------+------------+---------+
Output:
+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1          | 2   |
| 2          | 4   |
+------------+-----+
Explanation:
Teacher 1:
  - They teach subject 2 in departments 3 and 4.
  - They teach subject 3 in department 3.
Teacher 2:
  - They teach subject 1 in department 1.
  - They teach subject 2 in department 1.
  - They teach subject 3 in department 1.
  - They teach subject 4 in department 1.
*/
WITH TeacherSubjects AS (
    SELECT 1 AS teacher_id, 2 AS subject_id, 3 AS dept_id UNION ALL
    SELECT 1 AS teacher_id, 2 AS subject_id, 4 AS dept_id UNION ALL
    SELECT 1 AS teacher_id, 3 AS subject_id, 3 AS dept_id UNION ALL
    SELECT 2 AS teacher_id, 1 AS subject_id, 1 AS dept_id UNION ALL
    SELECT 2 AS teacher_id, 2 AS subject_id, 1 AS dept_id UNION ALL
    SELECT 2 AS teacher_id, 3 AS subject_id, 1 AS dept_id UNION ALL
    SELECT 2 AS teacher_id, 4 AS subject_id, 1 AS dept_id
)
SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) cnt
FROM
    TeacherSubjects
GROUP BY teacher_id
"""
import pandas as pd

# Simulating the TeacherSubjects table
teacher_subjects = pd.DataFrame({
    'teacher_id': [1, 1, 1, 2, 2, 2, 2],
    'subject_id': [2, 2, 3, 1, 2, 3, 4],
    'dept_id': [3, 4, 3, 1, 1, 1, 1]
})

# Counting distinct subjects each teacher teaches
teacher_subject_count = teacher_subjects.groupby('teacher_id')['subject_id'].nunique().reset_index()
teacher_subject_count.columns = ['teacher_id', 'cnt']

# Displaying the result
print(teacher_subject_count)

"""

Table: Students

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one student in the school.


Table: Subjects

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
subject_name is the primary key (column with unique values) for this table.
Each row of this table contains the name of one subject in the school.


Table: Examinations

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each student from the Students table takes every course from the Subjects table.
Each row of this table indicates that a student with ID student_id attended the exam of subject_name.


Write a solution to find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name.

The result format is in the following example.



Example 1:

Input:
Students table:
+------------+--------------+
| student_id | student_name |
+------------+--------------+
| 1          | Alice        |
| 2          | Bob          |
| 13         | John         |
| 6          | Alex         |
+------------+--------------+
Subjects table:
+--------------+
| subject_name |
+--------------+
| Math         |
| Physics      |
| Programming  |
+--------------+
Examinations table:
+------------+--------------+
| student_id | subject_name |
+------------+--------------+
| 1          | Math         |
| 1          | Physics      |
| 1          | Programming  |
| 2          | Programming  |
| 1          | Physics      |
| 1          | Math         |
| 13         | Math         |
| 13         | Programming  |
| 13         | Physics      |
| 2          | Math         |
| 1          | Math         |
+------------+--------------+
Output:
+------------+--------------+--------------+----------------+
| student_id | student_name | subject_name | attended_exams |
+------------+--------------+--------------+----------------+
| 1          | Alice        | Math         | 3              |
| 1          | Alice        | Physics      | 2              |
| 1          | Alice        | Programming  | 1              |
| 2          | Bob          | Math         | 1              |
| 2          | Bob          | Physics      | 0              |
| 2          | Bob          | Programming  | 1              |
| 6          | Alex         | Math         | 0              |
| 6          | Alex         | Physics      | 0              |
| 6          | Alex         | Programming  | 0              |
| 13         | John         | Math         | 1              |
| 13         | John         | Physics      | 1              |
| 13         | John         | Programming  | 1              |
+------------+--------------+--------------+----------------+
Explanation:
The result table should contain all students and all subjects.
Alice attended the Math exam 3 times, the Physics exam 2 times, and the Programming exam 1 time.
Bob attended the Math exam 1 time, the Programming exam 1 time, and did not attend the Physics exam.
Alex did not attend any exams.
John attended the Math exam 1 time, the Physics exam 1 time, and the Programming exam 1 time.
*/

WITH Students AS (
  SELECT 1 AS student_id, 'Alice' AS student_name UNION ALL
  SELECT 2 AS student_id, 'Bob' AS student_name UNION ALL
  SELECT 13 AS student_id, 'John' AS student_name UNION ALL
  SELECT 6 AS student_id, 'Alex' AS student_name
),
Subjects AS (
  SELECT 'Math' AS subject_name UNION ALL
  SELECT 'Physics' AS subject_name UNION ALL
  SELECT 'Programming' AS subject_name
),
Examinations AS (
  SELECT 1 AS student_id, 'Math' AS subject_name UNION ALL
  SELECT 1 AS student_id, 'Physics' AS subject_name UNION ALL
  SELECT 1 AS student_id, 'Programming' AS subject_name UNION ALL
  SELECT 2 AS student_id, 'Programming' AS subject_name UNION ALL
  SELECT 1 AS student_id, 'Physics' AS subject_name UNION ALL
  SELECT 1 AS student_id, 'Math' AS subject_name UNION ALL
  SELECT 13 AS student_id, 'Math' AS subject_name UNION ALL
  SELECT 13 AS student_id, 'Programming' AS subject_name UNION ALL
  SELECT 13 AS student_id, 'Physics' AS subject_name UNION ALL
  SELECT 2 AS student_id, 'Math' AS subject_name UNION ALL
  SELECT 1 AS student_id, 'Math' AS subject_name
)

-- Query to combine Students and Examinations tables
SELECT
    st.student_id,
    st.student_name,
    sub.subject_name,
    COUNT(e.student_id)
FROM
    Students st
CROSS JOIN
    Subjects sub
LEFT JOIN
    Examinations e ON st.student_id=e.student_id AND sub.subject_name=e.subject_name
GROUP BY st.student_id, st.student_name, sub.subject_name
"""

import pandas as pd

# Sample data for Students table
students_data = {
    'student_id': [1, 2, 13, 6],
    'student_name': ['Alice', 'Bob', 'John', 'Alex']
}

# Sample data for Subjects table
subjects_data = {
    'subject_name': ['Math', 'Physics', 'Programming']
}

# Sample data for Examinations table
examinations_data = {
    'student_id': [1, 1, 1, 2, 1, 1, 13, 13, 13, 2, 1],
    'subject_name': ['Math', 'Physics', 'Programming', 'Programming', 'Physics', 'Math', 'Math', 'Programming', 'Physics', 'Math', 'Math']
}

# Convert data to pandas DataFrames
df_students = pd.DataFrame(students_data)
df_subjects = pd.DataFrame(subjects_data)
df_examinations = pd.DataFrame(examinations_data)

# Perform a cross join between Students and Subjects
df_students['key'] = 1
df_subjects['key'] = 1
df_cross = pd.merge(df_students, df_subjects, on='key').drop('key', axis=1)

# Perform a left join with Examinations to count the attended exams
df_result = pd.merge(df_cross, df_examinations, on=['student_id', 'subject_name'], how='left')

# Group by to count the number of attended exams
df_final = df_result.groupby(['student_id', 'student_name', 'subject_name']).size().reset_index(name='attended_exams')

# Display the final DataFrame
print(df_final)

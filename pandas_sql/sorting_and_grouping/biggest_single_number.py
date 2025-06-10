"""/*
Table: MyNumbers

+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.


A single number is a number that appeared only once in the MyNumbers table.

Find the largest single number. If there is no single number, report null.

The result format is in the following example.



Example 1:

Input:
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
+-----+
Output:
+-----+
| num |
+-----+
| 6   |
+-----+
Explanation: The single numbers are 1, 4, 5, and 6.
Since 6 is the largest single number, we return it.
Example 2:

Input:
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 7   |
| 7   |
| 3   |
| 3   |
| 3   |
+-----+
Output:
+------+
| num  |
+------+
| null |
+------+
Explanation: There are no single numbers in the input table so we return null.
*/
WITH MyNumbers AS (
    SELECT 8 AS num UNION ALL
    SELECT 8 AS num UNION ALL
    SELECT 3 AS num UNION ALL
    SELECT 3 AS num UNION ALL
    SELECT 1 AS num UNION ALL
    SELECT 4 AS num UNION ALL
    SELECT 5 AS num UNION ALL
    SELECT 6 AS num
)
SELECT
    MAX(num) num
FROM (
    SELECT
        num
    FROM
        MyNumbers
    GROUP BY
        num
    HAVING
        COUNT(*) = 1
)


"""

import pandas as pd

# Sample data for MyNumbers table
numbers_data = {
    'num': [8, 8, 3, 3, 1, 4, 5, 6]
}

# Convert data to pandas DataFrame
df_numbers = pd.DataFrame(numbers_data)

# Group by the 'num' column and count the occurrences of each number
df_grouped = df_numbers.groupby('num').size().reset_index(name='count')

# Filter out the numbers that appear more than once
df_single_occurrences = df_grouped[df_grouped['count'] == 1]

# Check if there are any single occurrence numbers
if not df_single_occurrences.empty:
    # Find the maximum number from the filtered list
    max_single_number = df_single_occurrences['num'].max()
    result = pd.DataFrame({'num': [max_single_number]})
else:
    # Return null if there are no single occurrence numbers
    result = pd.DataFrame({'num': [None]})

# Display the final DataFrame
print(result)




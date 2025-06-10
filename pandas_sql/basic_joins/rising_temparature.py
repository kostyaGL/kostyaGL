"""

Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.


Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Output:
+----+
| id |
+----+
| 2  |
| 4  |
+----+
Explanation:
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).
*/

WITH temperature_records AS (
  SELECT 1 AS id, DATE '2015-01-01' AS recordDate, 10 AS temperature UNION ALL
  SELECT 2 AS id, DATE '2015-01-02' AS recordDate, 25 AS temperature UNION ALL
  SELECT 3 AS id, DATE '2015-01-03' AS recordDate, 20 AS temperature UNION ALL
  SELECT 4 AS id, DATE '2015-01-04' AS recordDate, 30 AS temperature
)

-- Now you can query the CTE to see the data
SELECT
  tr.id
FROM
 temperature_records tr
JOIN temperature_records tr1 ON tr.recordDate = DATE_ADD(tr1.recordDate, INTERVAL 1 DAY)
WHERE tr.temperature > tr1.temperature
"""
import pandas as pd

# Sample data for Weather table
weather_data = {
    'id': [1, 2, 3, 4],
    'recordDate': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04'],
    'temperature': [10, 25, 20, 30]
}

# Convert data to pandas DataFrame
df_weather = pd.DataFrame(weather_data)

# Convert 'recordDate' to datetime type
df_weather['recordDate'] = pd.to_datetime(df_weather['recordDate'])

# Sort the DataFrame by 'recordDate' to ensure correct order
df_weather = df_weather.sort_values('recordDate')

# Calculate the difference in temperature with the previous day
df_weather['temp_diff'] = df_weather['temperature'].diff()

# Select rows where the temperature was higher than the previous day
df_result = df_weather[df_weather['temp_diff'] > 0]

# Select and display the 'id' column of the resulting DataFrame
df_final = df_result[['id']]
print(df_final)

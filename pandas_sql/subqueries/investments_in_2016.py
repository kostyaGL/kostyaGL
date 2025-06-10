"""
Table: Insurance

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| pid         | int   |
| tiv_2015    | float |
| tiv_2016    | float |
| lat         | float |
| lon         | float |
+-------------+-------+
pid is the primary key (column with unique values) for this table.
Each row of this table contains information about one policy where:
pid is the policyholder's policy ID.
tiv_2015 is the total investment value in 2015 and tiv_2016 is the total investment value in 2016.
lat is the latitude of the policy holder's city. It's guaranteed that lat is not NULL.
lon is the longitude of the policy holder's city. It's guaranteed that lon is not NULL.


Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:

have the same tiv_2015 value as one or more other policyholders, and
are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
Round tiv_2016 to two decimal places.

The result format is in the following example.
*/

WITH Insurance AS (
    SELECT 1 AS pid, 10 AS tiv_2015, 5 AS tiv_2016, 10 AS lat, 10 AS lon
    UNION ALL
    SELECT 2, 20, 20, 20, 20
    UNION ALL
    SELECT 3, 10, 30, 20, 20
    UNION ALL
    SELECT 4, 10, 40, 40, 40
)
-- Write your PostgreSQL query statement below
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016 FROM (select *,
        count(concat(lat, lon))over(partition by lat, lon order by lat, lon) numb,
        count(tiv_2015)over(partition by tiv_2015 order by tiv_2015) tf
    from Insurance)
WHERE numb=1 AND tf > 1
"""
import pandas as pd

# Simulating the Insurance table
data = {
    'pid': [1, 2, 3, 4],
    'tiv_2015': [10, 20, 10, 10],
    'tiv_2016': [5, 20, 30, 40],
    'lat': [10, 20, 20, 40],
    'lon': [10, 20, 20, 40]
}

insurance_df = pd.DataFrame(data)

# Step 2: Replicate window functions using pandas
insurance_df['numb'] = insurance_df.groupby(['lat', 'lon']).transform('count')
insurance_df['tf'] = insurance_df.groupby('tiv_2015')['tiv_2015'].transform('count')

# Step 3: Apply filtering conditions
filtered_df = insurance_df[(insurance_df['numb'] == 1) & (insurance_df['tf'] > 1)]

# Step 4: Aggregate and round the sum of tiv_2016
tiv_2016_sum = filtered_df['tiv_2016'].sum()
rounded_tiv_2016_sum = round(tiv_2016_sum, 2)

# Prepare the output in the required format
output_df = pd.DataFrame({'tiv_2016': [rounded_tiv_2016_sum]})

print(output_df)

# /*
#
# Pandas Schema
# Table Activities:
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | sell_date   | date    |
# | product     | varchar |
# +-------------+---------+
# There is no primary key (column with unique values) for this table. It may contain duplicates.
# Each row of this table contains the product name and the date it was sold in a market.
#
#
# Write a solution to find for each date the number of different products sold and their names.
#
# The sold products names for each date should be sorted lexicographically.
#
# Return the result table ordered by sell_date.
#
# The result format is in the following example.
#
#
#
# Example 1:
#
# Input:
# Activities table:
# +------------+------------+
# | sell_date  | product     |
# +------------+------------+
# | 2020-05-30 | Headphone  |
# | 2020-06-01 | Pencil     |
# | 2020-06-02 | Mask       |
# | 2020-05-30 | Basketball |
# | 2020-06-01 | Bible      |
# | 2020-06-02 | Mask       |
# | 2020-05-30 | T-Shirt    |
# +------------+------------+
# Output:
# +------------+----------+------------------------------+
# | sell_date  | num_sold | products                     |
# +------------+----------+------------------------------+
# | 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
# | 2020-06-01 | 2        | Bible,Pencil                 |
# | 2020-06-02 | 1        | Mask                         |
# +------------+----------+------------------------------+
# Explanation:
# For 2020-05-30, Sold items were (Headphone, Basketball, T-shirt), we sort them lexicographically and separate them by a comma.
# For 2020-06-01, Sold items were (Pencil, Bible), we sort them lexicographically and separate them by a comma.
# For 2020-06-02, the Sold item is (Mask), we just return it.
# */
# WITH Activities AS (
#     SELECT '2020-05-30' AS sell_date, 'Headphone' AS product
#     UNION ALL
#     SELECT '2020-06-01', 'Pencil'
#     UNION ALL
#     SELECT '2020-06-02', 'Mask'
#     UNION ALL
#     SELECT '2020-05-30', 'Basketball'
#     UNION ALL
#     SELECT '2020-06-01', 'Bible'
#     UNION ALL
#     SELECT '2020-06-02', 'Mask'
#     UNION ALL
#     SELECT '2020-05-30', 'T-Shirt'
# )
# SELECT sell_date, count(*) number_of_sold, string_agg(product, ',')products FROM Activities group by sell_date;

import pandas as pd

# Sample data
data = {
    'sell_date': ['2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30'],
    'product': ['Headphone', 'Pencil', 'Mask', 'Basketball', 'Bible', 'Mask', 'T-Shirt']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert sell_date to datetime type
df['sell_date'] = pd.to_datetime(df['sell_date'])

# Group by sell_date, aggregate product names and count unique products
grouped = df.groupby('sell_date').agg({'product': lambda x: sorted(set(x))})

# Count number of different products
grouped['num_sold'] = grouped['product'].apply(len)

# Join product names with comma separator
grouped['products'] = grouped['product'].str.join(',')

# Drop the temporary 'product' column
grouped.drop(columns=['product'], inplace=True)

# Reset index to make sell_date a column again
grouped = grouped.reset_index()

# Display the result ordered by sell_date
print(grouped)

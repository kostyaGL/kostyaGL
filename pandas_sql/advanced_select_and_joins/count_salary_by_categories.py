# /*
# Table: Accounts
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | account_id  | int  |
# | income      | int  |
# +-------------+------+
# account_id is the primary key (column with unique values) for this table.
# Each row contains information about the monthly income for one bank account.
#
#
# Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:
#
# "Low Salary": All the salaries strictly less than $20000.
# "Average Salary": All the salaries in the inclusive range [$20000, $50000].
# "High Salary": All the salaries strictly greater than $50000.
# The result table must contain all three categories. If there are no accounts in a category, return 0.
#
# Return the result table in any order.
#
# The result format is in the following example.
#
#
#
# Example 1:
#
# Input:
# Accounts table:
# +------------+--------+
# | account_id | income |
# +------------+--------+
# | 3          | 108939 |
# | 2          | 12747  |
# | 8          | 87709  |
# | 6          | 91796  |
# +------------+--------+
# Output:
# +----------------+----------------+
# | category       | accounts_count |
# +----------------+----------------+
# | Low Salary     | 1              |
# | Average Salary | 0              |
# | High Salary    | 3              |
# +----------------+----------------+
# Explanation:
# Low Salary: Account 2.
# Average Salary: No accounts.
# High Salary: Accounts 3, 6, and 8.
# */
import pandas as pd

# Define the data in a dictionary format
data = {
    'account_id': [3, 2, 8, 6],
    'income': [108939, 12747, 87709, 91796]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Define salary categories and calculate counts
low_salary_count = df[df['income'] < 20000]['income'].count()
average_salary_count = df[df['income'].between(20000, 50000)]['income'].count()
high_salary_count = df[df['income'] > 50000]['income'].count()

# Create result DataFrame
result_df = pd.DataFrame({
    'category': ['Low Salary', 'Average Salary', 'High Salary'],
    'accounts_count': [low_salary_count, average_salary_count, high_salary_count]
})

# Display the result
print(result_df)

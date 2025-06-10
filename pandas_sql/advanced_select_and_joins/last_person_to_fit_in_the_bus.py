# /*
# Table: Queue
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | person_id   | int     |
# | person_name | varchar |
# | weight      | int     |
# | turn        | int     |
# +-------------+---------+
# person_id column contains unique values.
# This table has the information about all people waiting for a bus.
# The person_id and turn columns will contain all numbers from 1 to n, where n is the number of rows in the table.
# turn determines the order of which the people will board the bus, where turn=1 denotes the first person to board and turn=n denotes the last person to board.
# weight is the weight of the person in kilograms.
#
#
# There is a queue of people waiting to board a bus. However, the bus has a weight limit of 1000 kilograms, so there may be some people who cannot board.
#
# Write a solution to find the person_name of the last person that can fit on the bus without exceeding the weight limit. The test cases are generated such that the first person does not exceed the weight limit.
#
# The result format is in the following example.
#
#
#
# Example 1:
#
# Input:
# Queue table:
# +-----------+-------------+--------+------+
# | person_id | person_name | weight | turn |
# +-----------+-------------+--------+------+
# | 5         | Alice       | 250    | 1    |
# | 4         | Bob         | 175    | 5    |
# | 3         | Alex        | 350    | 2    |
# | 6         | John Cena   | 400    | 3    |
# | 1         | Winston     | 500    | 6    |
# | 2         | Marie       | 200    | 4    |
# +-----------+-------------+--------+------+
# Output:
# +-------------+
# | person_name |
# +-------------+
# | John Cena   |
# +-------------+
# Explanation: The folowing table is ordered by the turn for simplicity.
# +------+----+-----------+--------+--------------+
# | Turn | ID | Name      | Weight | Total Weight |
# +------+----+-----------+--------+--------------+
# | 1    | 5  | Alice     | 250    | 250          |
# | 2    | 3  | Alex      | 350    | 600          |
# | 3    | 6  | John Cena | 400    | 1000         | (last person to board)
# | 4    | 2  | Marie     | 200    | 1200         | (cannot board)
# | 5    | 4  | Bob       | 175    | ___          |
# | 6    | 1  | Winston   | 500    | ___          |
# +------+----+-----------+--------+--------------+
# */
import pandas as pd

# Define the data in a dictionary format
data = {
    'person_id': [5, 4, 3, 6, 1, 2],
    'person_name': ['Alice', 'Bob', 'Alex', 'John Cena', 'Winston', 'Marie'],
    'weight': [250, 175, 350, 400, 500, 200],
    'turn': [1, 5, 2, 3, 6, 4]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Sort by turn to simulate boarding order
df = df.sort_values(by='turn')

# Calculate cumulative weight
df['cumulative_weight'] = df['weight'].cumsum()

# Find the last person that fits within the weight limit (1000 kg)
last_person = df[df['cumulative_weight'] <= 1000].iloc[-1]

# Display the result
print(last_person['person_name'])

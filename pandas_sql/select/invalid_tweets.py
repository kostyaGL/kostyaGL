"""
Table: Tweets

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
This table contains all the tweets in a social media app.


Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Tweets table:
+----------+----------------------------------+
| tweet_id | content                          |
+----------+----------------------------------+
| 1        | Vote for Biden                   |
| 2        | Let us make America great again! |
+----------+----------------------------------+
Output:
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
Explanation:
Tweet 1 has length = 14. It is a valid tweet.
Tweet 2 has length = 32. It is an invalid tweet.
*/

WITH cte AS (
  SELECT 1 AS tweet_id, 'Vote for Biden' AS content UNION ALL
  SELECT 2 AS tweet_id, 'Let us make America great again!' AS content
)

SELECT tweet_id
FROM cte
WHERE length(content) >= 15;
"""

import pandas as pd

# Sample data for Tweets table
tweets_data = {
    'tweet_id': [1, 2],
    'content': ['Vote for Biden', 'Let us make America great again!']
}

# Convert data to pandas DataFrame
df_tweets = pd.DataFrame(tweets_data)

# Filter the DataFrame to include only tweets with content length >= 15
df_filtered = df_tweets[df_tweets['content'].str.len() >= 15]

# Select the required column
df_result = df_filtered[['tweet_id']]

# Display the final DataFrame
print(df_result)

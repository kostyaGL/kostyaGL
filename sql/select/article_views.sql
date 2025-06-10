/*

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date.
Note that equal author_id and viewer_id indicate the same person.


Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

The result format is in the following example.



Example 1:

Input:
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output:
+------+
| id   |
+------+
| 4    |
| 7    |
+------+

*/
WITH cte AS (
  SELECT 1 AS article_id, 3 AS author_id, 5 AS viewer_id, '2019-08-01' AS view_date UNION ALL
  SELECT 1 AS article_id, 3 AS author_id, 6 AS viewer_id, '2019-08-02' AS view_date UNION ALL
  SELECT 2 AS article_id, 7 AS author_id, 7 AS viewer_id, '2019-08-01' AS view_date UNION ALL
  SELECT 2 AS article_id, 7 AS author_id, 6 AS viewer_id, '2019-08-02' AS view_date UNION ALL
  SELECT 4 AS article_id, 7 AS author_id, 1 AS viewer_id, '2019-07-22' AS view_date UNION ALL
  SELECT 3 AS article_id, 4 AS author_id, 4 AS viewer_id, '2019-07-21' AS view_date UNION ALL
  SELECT 3 AS article_id, 4 AS author_id, 4 AS viewer_id, '2019-07-21' AS view_date
)

SELECT
  DISTINCT cte.author_id AS id
FROM
  cte
WHERE cte.author_id=cte.viewer_id;

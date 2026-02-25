# Write your MySQL query statement below
# finding ID's of invalid tweets
# invalid tweet = num chars in content > 15

SELECT tweet_id FROM Tweets
WHERE LENGTH(content) > 15;
# Write your MySQL query statement below
# find customers where the referree_id is not 2 and they have no been referred
SELECT name 
FROM customer
WHERE referee_id != 2 OR referee_id is NULL;
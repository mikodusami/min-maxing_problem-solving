# Write your MySQL query statement below
# find ids of products that are low fat and recyclable

SELECT product_id
FROM Products
WHERE low_fats = "Y" AND recyclable = "Y"
# Write your MySQL query statement below
# finding ALL authors that viewed at least one of their OWN articles
# RETURN result table SORTED by id in asending order

# the table may have duplicate rows
# equal author_id and viewer_id indiciate same person

# we are finding all articles where viewer_id == author_id sorted by id in ascending order and reutnr the authorid


SELECT DISTINCT author_id AS id FROM Views
WHERE author_id = viewer_id 
ORDER BY author_id ASC;


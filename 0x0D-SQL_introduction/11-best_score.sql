-- This script displays the score and name columns only, filter the result to include only scores that are greater than or equal to 10 and order the record by higher scores
SELECT score, name FROM second_table where score>=10 ORDER BY score DESC;

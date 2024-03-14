-- This script displays the score and the number of the occurence of each value of the score
SELECT score, COUNT(`score`) AS 'number' FROM second_table GROUP BY score DESC;

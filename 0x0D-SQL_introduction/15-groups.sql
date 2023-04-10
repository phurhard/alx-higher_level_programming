-- Lists the number of records with the same score
-- displays score and the number of occurence

SELECT score, COUNT(score) AS number FROM second_table GROUP BY score;

-- This lists all table that has score >= 10 in high scores to low scores
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

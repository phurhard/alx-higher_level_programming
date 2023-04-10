-- Lists all records in the table
-- Dont list rows without name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

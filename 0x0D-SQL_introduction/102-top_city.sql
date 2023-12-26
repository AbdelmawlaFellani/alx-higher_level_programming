-- Display the top 3 of cities temperature during July and August
SELECT * FROM temperatures WHERE month BETWEEN 7 AND 8 ORDER BY value DESC LIMIT 3;

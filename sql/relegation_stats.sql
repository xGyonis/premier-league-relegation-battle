SELECT season_id, COUNT(*) AS relegated_under_45pts
FROM league_tables
WHERE was_relegated = TRUE AND points < 45
GROUP BY season_id
ORDER BY season_id;

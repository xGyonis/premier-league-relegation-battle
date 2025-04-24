# Falling Flat: The Decline of the Premier League Relegation Battle (2000–2025)

This project investigates the diminishing excitement around the Premier League relegation battle from the 2000–01 season to 2024–25. Using data engineering and statistical analysis, this project aims to reveal trends in how newly promoted teams struggle to survive, how early-season predictability has reduced the drama of the run-in, and how financial disparity has widened the gap between bottom-tier and mid-table clubs.

## Data Engineering

### Core Tables:

seasons (season_id, year_start, year_end)

teams (team_id, name)

matches (match_id, season_id, date, home_team_id, away_team_id, home_goals, away_goals)

league_tables (season_id, team_id, position, points, goal_difference, wins, draws, losses)

promotions_relegations (season_id, team_id, was_promoted, was_relegated)

### Data Sources

FBref (stats per season, standings, match results)

Wikipedia (promotion/relegation teams)

Understat (advanced stats like xG)

Transfermarkt (squad value, transfers, injuries)

### Ingestion & Storage

Use Python (requests, BeautifulSoup, or Selenium) to scrape data or pull from CSVs.

Use pandas for initial wrangling, then insert clean data into a SQL database.

Use SQLite or PostgreSQL for storage.

Normalize tables, add indices on season/team columns for efficient querying.

## Data Analysis: 

### Questions to ask around the relegation battle?

How often do newly promoted teams get relegated in their first season?

What’s the average point total of the 18th–20th place teams over time?

How many games before the end of the season are the bottom 3 effectively “locked in”?

Has the point gap between 17th and 18th widened over time?

Has financial disparity played a role in this trend?

### Python Tools

pandas, numpy for computation

matplotlib, seaborn, plotly for data viz

scikit-learn for any predictive modeling (e.g., to model likelihood of relegation)

sqlalchemy or psycopg2 for connecting Python to your database

## Conclusion:

Statistically demonstrate that the relegation battle has become more predictable.

Showcase that financial inequality and promotion/relegation churn have played a role.

Possibly recommend how the Premier League can restore the jeopardy.

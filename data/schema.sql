CREATE TABLE seasons (
    season_id SERIAL PRIMARY KEY,
    year_start INT,
    year_end INT
);

CREATE TABLE teams (
    team_id SERIAL PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE matches (
    match_id SERIAL PRIMARY KEY,
    season_id INT REFERENCES seasons(season_id),
    date DATE,
    home_team_id INT REFERENCES teams(team_id),
    away_team_id INT REFERENCES teams(team_id),
    home_goals INT,
    away_goals INT
);

CREATE TABLE league_tables (
    id SERIAL PRIMARY KEY,
    season_id INT REFERENCES seasons(season_id),
    team_id INT REFERENCES teams(team_id),
    position INT,
    points INT,
    goal_difference INT,
    wins INT,
    draws INT,
    losses INT
);

CREATE TABLE promotions_relegations (
    id SERIAL PRIMARY KEY,
    season_id INT REFERENCES seasons(season_id),
    team_id INT REFERENCES teams(team_id),
    was_promoted BOOLEAN,
    was_relegated BOOLEAN
);
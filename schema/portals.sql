CREATE TABLE player(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    UNIQUE(name)
);

CREATE TABLE game(
    id SERIAL PRIMARY KEY,
    name VARCHAR(256),
    date_created TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE(name)
);

CREATE TABLE chatlog(
    id SERIAL PRIMARY KEY,
    game_id INTEGER NOT NULL REFERENCES game(id),
    player_id INTEGER NOT NULL REFERENCES player(id),
    message TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT now()
);

INSERT INTO player(name) VALUES ('guide');
INSERT INTO game(name) VALUES ('Test Game');

CREATE TABLE player(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE(name)
);

CREATE TABLE game(
    id SERIAL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
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

-- Temp password: guide
INSERT INTO player(name, password) VALUES ('guide', '$2b$12$rfudtuKq7T0.PyyafERRJ.2lAtjv92Dh.tR8uY/0.j4PBzEYywDxC');
INSERT INTO player(name, password) VALUES ('tester', '$2y$12$k90XEfRb7O7rVnvpo05ixOgV8NIfqlNh06zQZrKaQLaArMzoHM4hW');
INSERT INTO game(name) VALUES ('Test Game');

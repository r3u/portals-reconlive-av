CREATE TABLE actor(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE(name)
);

CREATE TABLE world(
    id SERIAL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE(name)
);

CREATE TABLE session(
    id SERIAL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE(name)
);

CREATE TABLE chatlog_entry(
    id SERIAL PRIMARY KEY,
    session_id INTEGER NOT NULL REFERENCES session(id),
    actor_id INTEGER NOT NULL REFERENCES actor(id),
    message TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT now()
);

-- Temp password: guide
INSERT INTO actor(name, password) VALUES ('guide', '$2b$12$rfudtuKq7T0.PyyafERRJ.2lAtjv92Dh.tR8uY/0.j4PBzEYywDxC');
INSERT INTO actor(name, password) VALUES ('tester', '$2y$12$k90XEfRb7O7rVnvpo05ixOgV8NIfqlNh06zQZrKaQLaArMzoHM4hW');
INSERT INTO session(name) VALUES ('Test Session');

DROP TYPE IF EXISTS actor_role CASCADE;
CREATE TYPE actor_role AS ENUM('guide', 'scout');


DROP TABLE IF EXISTS actor CASCADE;
CREATE TABLE actor(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    role actor_role NOT NULL,
    password VARCHAR(255) NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE(name)
);


DROP TABLE IF EXISTS world CASCADE;
CREATE TABLE world(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE(name)
);


DROP TABLE IF EXISTS location CASCADE;
CREATE TABLE location(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    world_id INTEGER NOT NULL REFERENCES world(id),
    date_created TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE(name, world_id)
);


DROP TABLE IF EXISTS path CASCADE;
CREATE TABLE path(
    id SERIAL PRIMARY KEY,
    start_id INTEGER NOT NULL REFERENCES location(id) ON UPDATE CASCADE ON DELETE CASCADE,
    destination_id INTEGER NOT NULL REFERENCES location(id) ON UPDATE CASCADE ON DELETE CASCADE,
    UNIQUE (start_id, destination_id)
);
CREATE INDEX path_start_id_idx ON path(start_id);
CREATE INDEX path_destination_id_idx ON path(destination_id);
ALTER TABLE path ADD CONSTRAINT path_check_no_self_loops CHECK (start_id <> destination_id);


DROP TABLE path_description;
CREATE TABLE path_description(
    id SERIAL PRIMARY KEY,
    path_id INTEGER NOT NULL REFERENCES path(id),
    description TEXT,
    date_created TIMESTAMP NOT NULL DEFAULT now()
);


DROP TABLE IF EXISTS session CASCADE;
CREATE TABLE session(
    id SERIAL PRIMARY KEY,
    code VARCHAR(255) NOT NULL,
    active boolean NOT NULL DEFAULT false,
    current_location_id INTEGER NOT NULL REFERENCES location(id),
    date_created TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE(code)
);
CREATE UNIQUE INDEX ON session(active) WHERE active = true;


DROP TABLE IF EXISTS chatlog_entry CASCADE;
CREATE TABLE chatlog_entry(
    id SERIAL PRIMARY KEY,
    session_id INTEGER NOT NULL REFERENCES session(id),
    actor_id INTEGER NOT NULL REFERENCES actor(id),
    message TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT now()
);


DROP TABLE IF EXISTS media_asset CASCADE;
CREATE TABLE media_asset(
    id SERIAL PRIMARY KEY,
    filename TEXT NOT NULL,
    hash_sha256 VARCHAR(64) NOT NULL,
    content BYTEA NOT NULL,
    mime_type TEXT NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT now()
);


DROP TABLE IF EXISTS tag CASCADE;
CREATE TABLE tag(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);


DROP TABLE IF EXISTS media_asset_tags CASCADE;
CREATE TABLE media_asset_tags(
    media_asset_id INT NOT NULL REFERENCES media_asset(id),
    tag_id INT NOT NULL REFERENCES tag(id)
);


-- guide default password: guide
INSERT INTO actor(name, role, password)
VALUES (
    'guide',
    'guide',
    '$2b$12$rfudtuKq7T0.PyyafERRJ.2lAtjv92Dh.tR8uY/0.j4PBzEYywDxC'
);
-- tester default password: tester
INSERT INTO actor(name, role, password) VALUES (
    'tester',
    'scout',
    '$2y$12$k90XEfRb7O7rVnvpo05ixOgV8NIfqlNh06zQZrKaQLaArMzoHM4hW'
);

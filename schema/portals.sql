CREATE TABLE actor(
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name)
);


CREATE TABLE world(
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name)
);


CREATE TABLE location(
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    world_id INTEGER NOT NULL REFERENCES world(id),
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name, world_id)
);


CREATE TABLE path(
    id INTEGER PRIMARY KEY,
    start_id INTEGER NOT NULL REFERENCES location(id) ON UPDATE CASCADE ON DELETE CASCADE,
    destination_id INTEGER NOT NULL REFERENCES location(id) ON UPDATE CASCADE ON DELETE CASCADE,
    description TEXT NOT NULL,
    UNIQUE (start_id, destination_id)
);
CREATE INDEX path_start_id_idx ON path(start_id);
CREATE INDEX path_destination_id_idx ON path(destination_id);
--ALTER TABLE path ADD CONSTRAINT path_check_no_self_loops CHECK (start_id <> destination_id);


CREATE TABLE location_info(
    id INTEGER PRIMARY KEY,
    location_id INTEGER NOT NULL REFERENCES location(id),
    info TEXT NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE session(
    id INTEGER PRIMARY KEY,
    code VARCHAR(255) NOT NULL,
    active boolean NOT NULL DEFAULT false,
    current_location_id INTEGER NOT NULL REFERENCES location(id),
    previous_location_id INTEGER NOT NULL REFERENCES location(id),
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(code)
);
--CREATE UNIQUE INDEX ON session(active) WHERE active = true;


CREATE TABLE chatlog_entry(
    id INTEGER PRIMARY KEY,
    session_id INTEGER NOT NULL REFERENCES session(id),
    actor_id INTEGER NOT NULL REFERENCES actor(id),
    message TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
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

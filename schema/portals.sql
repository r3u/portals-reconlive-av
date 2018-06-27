DROP TABLE IF EXISTS actor CASCADE;
CREATE TABLE actor(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE(name)
);

DROP TABLE IF EXISTS world CASCADE;
CREATE TABLE world(
    id SERIAL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE(name)
);

DROP TABLE IF EXISTS location CASCADE;
CREATE TABLE location(
    id SERIAL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    world_id INTEGER NOT NULL REFERENCES world(id),
    date_created TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE(name, world_id)
);

DROP TABLE IF EXISTS path CASCADE;
CREATE TABLE path(
    a INTEGER NOT NULL REFERENCES location(id) ON UPDATE CASCADE ON DELETE CASCADE,
    b INTEGER NOT NULL REFERENCES location(id) ON UPDATE CASCADE ON DELETE CASCADE,
    PRIMARY KEY (a, b)
);
CREATE INDEX path_a_idx ON path(a);
CREATE INDEX path_b_idx ON path(b);
ALTER TABLE path ADD CONSTRAINT path_check_no_self_loops CHECK (a <> b);

DROP TABLE IF EXISTS session CASCADE;
CREATE TABLE session(
    id SERIAL PRIMARY KEY,
    code VARCHAR(256) NOT NULL,
    world_id INTEGER NOT NULL REFERENCES world(id),
    date_created TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE(code)
);

DROP TABLE IF EXISTS chatlog_entry CASCADE;
CREATE TABLE chatlog_entry(
    id SERIAL PRIMARY KEY,
    session_id INTEGER NOT NULL REFERENCES session(id),
    actor_id INTEGER NOT NULL REFERENCES actor(id),
    message TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT now()
);


-- test data --
INSERT INTO world(name) VALUES('Test World');
-- guide default password: guide
INSERT INTO actor(name, password) VALUES ('guide', '$2b$12$rfudtuKq7T0.PyyafERRJ.2lAtjv92Dh.tR8uY/0.j4PBzEYywDxC');
-- tester default password: tester
INSERT INTO actor(name, password) VALUES ('tester', '$2y$12$k90XEfRb7O7rVnvpo05ixOgV8NIfqlNh06zQZrKaQLaArMzoHM4hW');

INSERT INTO session(code, world_id) VALUES ('TestSession', (SELECT id FROM world WHERE name = 'Test World'));

INSERT INTO location(name, world_id) VALUES ('Plaza', (SELECT id FROM world WHERE name = 'Test World'));
INSERT INTO location(name, world_id) VALUES ('Old Grand Hotel', (SELECT id FROM world WHERE name = 'Test World'));

INSERT INTO path(a, b) VALUES (
    (SELECT id FROM location WHERE name = 'Plaza'),
    (SELECT id FROM location WHERE name = 'Old Grand Hotel')
);
INSERT INTO path(a, b) VALUES (
    (SELECT id FROM location WHERE name = 'Old Grand Hotel'),
    (SELECT id FROM location WHERE name = 'Plaza')
);


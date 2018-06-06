CREATE TABLE chatlog(
    id SERIAL PRIMARY KEY,
    message TEXT,
    timestamp TIMESTAMP NOT NULL DEFAULT now()
);

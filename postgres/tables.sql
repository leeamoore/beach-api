CREATE TABLE IF NOT EXISTS beach (
    id SERIAL,
    name VARCHAR NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS beach_image (
    id SERIAL,
    beach_id INTEGER REFERENCES beach(id),
    url VARCHAR NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS beach_comment (
    id SERIAL,
    beach_id INTEGER REFERENCES beach(id),
    user_id VARCHAR NOT NULL,
    comment VARCHAR NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS beach_rating (
    beach_id INTEGER REFERENCES beach(id),
    user_id VARCHAR NOT NULL,
    rating INTEGER CHECK (rating <= 5),
    PRIMARY KEY (beach_id, user_id)
);
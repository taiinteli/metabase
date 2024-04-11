CREATE TABLE IF NOT EXISTS medicoes (
    id SERIAL PRIMARY KEY,
    temperatura FLOAT NOT NULL,
    umidade FLOAT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO medicoes (
    temperatura,
    umidade
) VALUES (
    25.0,
    50.0
);

INSERT INTO medicoes (
    temperatura,
    umidade
) VALUES (
    26.0,
    51.0
);
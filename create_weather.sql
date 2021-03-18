
CREATE TABLE IF NOT EXISTS weather (
    city_namei TEXT,
    city_id TEXT,
    acquired_on TIMESTAMP,
    wind_speed_avg FLOAT,
    temperature_avg FLOAT,
    min_temperature FLOAT,
    max_temperature FLOAT,
    precipitation FLOAT,
    snow FLOAT
);

CREATE INDEX i_acquired_on
ON weather(acquired_on);

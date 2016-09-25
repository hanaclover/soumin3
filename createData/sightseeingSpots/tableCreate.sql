use Edmaps;
CREATE TABLE city_code(
    city_code tinyint(6) NOT NULL UNIQUE PRIMARY KEY,
    pref_code tinyint(2) NOT NULL,
    city_name char(7),
    city_name_spoken char(9),
    FOREIGN KEY(pref_code) REFERENCES pref_code(pref_code)
);

use Edmaps;
CREATE TABLE city_code(
    pref_code tinyint(2) NOT NULL UNIQUE PRIMARY KEY,
    pref_name char(4),
    pref_name_spoken char(6)
);

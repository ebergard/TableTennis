DROP TABLE IF EXISTS tournament;

CREATE TABLE tournament (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT UNIQUE NOT NULL,
  description TEXT NOT NULL
);
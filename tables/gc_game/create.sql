CREATE TABLE gc_game (
    id INTEGER PRIMARY KEY
  , game_id TEXT
  , gc_game_key TEXT
  , uri TEXT
  , gamebook TEXT
  , seasontype TEXT
  , week INTEGER
  , cp INTEGER
  , year INTEGER
  , gc_game_date TEXT
  , gc_game_time TEXT
  , day TEXT
  , state TEXT
  , gc_id INTEGER
  , FOREIGN KEY (gc_id) REFERENCES gc (id)
);

CREATE TABLE gc_game_team (
    id INTEGER PRIMARY KEY
  , abbr TEXT
  , fullname TEXT
  , link TEXT
  , standing TEXT
  , gc_game_id INTEGER
  , FOREIGN KEY (gc_game_id) REFERENCES gc_game (id)
)
;

CREATE TABLE gc_team (
    id INTEGER PRIMARY KEY
  , ah TEXT
  , standing TEXT
  , abbr TEXT
  , gc_id INTEGER
  , FOREIGN KEY (gc_id) REFERENCES gc (id)
)
;

CREATE TABLE gc_cur_team (
    id INTEGER PRIMARY KEY
  , ah TEXT
  , teamcode TEXT
  , abbr TEXT
  , fullname TEXT
  , comurl TEXT
  , cluburl TEXT
  , smscode TEXT
  , color TEXT
  , teamcolor TEXT
  , phone TEXT
  , standing TEXT
  , tout INTEGER
  , gc_cur_id INTEGER
  , FOREIGN KEY (gc_cur_id) REFERENCES gc_cur (id)
)
;

CREATE TABLE gc_cur (
    id INTEGER PRIMARY KEY
  , redzone INTEGER
  , rooftype TEXT
  , qtr TEXT
  , yl TEXT
  , clock TEXT
  , down INTEGER
  , togo INTEGER
  , posteam TEXT
  , stadium TEXT
  , gc_id INTEGER
  , FOREIGN KEY (gc_id) REFERENCES gc (id)
)
;

CREATE TABLE gc_cur_drive_play (
    id INTEGER PRIMARY KEY
  , gc_play_id TEXT
  , descr TEXT
  , posteam TEXT
  , qtr TEXT
  , time TEXT
  , down INTEGER
  , ydstogo INTEGER
  , yrdln TEXT
  , ydsnet INTEGER
  , note TEXT
  , sp INTEGER
  , gc_cur_drive_id INTEGER
  , FOREIGN KEY (gc_cur_drive_id) REFERENCES gc_cur_drive (id)
)
;

CREATE TABLE gc_cur_scrsummary (
    id INTEGER PRIMARY KEY
  , gc_play_id TEXT
  , qtr TEXT
  , team TEXT
  , scr_type TEXT
  , descr TEXT
  , gc_cur_id INTEGER
  , FOREIGN KEY (gc_cur_id) REFERENCES gc_cur (id)
)
;

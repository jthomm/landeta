CREATE TABLE gc_cur_scrsummary_player (
    id INTEGER PRIMARY KEY
  , gc_player_id TEXT
  , gc_player_name TEXT
  , gc_cur_scrsummary_id INTEGER
  , FOREIGN KEY (gc_cur_scrsummary_id) REFERENCES gc_cur_scrsummary (id)
)
;

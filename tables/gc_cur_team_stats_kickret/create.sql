CREATE TABLE gc_cur_team_stats_kickret (
    id INTEGER PRIMARY KEY
  , gc_player_id TEXT
  , name TEXT
  , ret INTEGER
  , avrg INTEGER
  , lng INTEGER
  , tds INTEGER
  , gc_cur_team_id INTEGER
  , FOREIGN KEY (gc_cur_team_id) REFERENCES gc_cur_team (id)
)
;

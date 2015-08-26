CREATE TABLE gc_cur_team_stats_punting (
    id INTEGER PRIMARY KEY
  , gc_player_id TEXT
  , name TEXT
  , pts INTEGER
  , yds INTEGER
  , avrg INTEGER
  , lng INTEGER
  , i20 INTEGER
  , gc_cur_team_id INTEGER
  , FOREIGN KEY (gc_cur_team_id) REFERENCES gc_cur_team (id)
)
;

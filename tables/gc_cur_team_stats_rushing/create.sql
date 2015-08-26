CREATE TABLE gc_cur_team_stats_rushing (
    id INTEGER PRIMARY KEY
  , gc_player_id TEXT
  , name TEXT
  , att INTEGER
  , yds INTEGER
  , tds INTEGER
  , lng INTEGER
  , lngtd INTEGER
  , twopta INTEGER
  , twoptm INTEGER
  , gc_cur_team_id INTEGER
  , FOREIGN KEY (gc_cur_team_id) REFERENCES gc_cur_team (id)
)
;

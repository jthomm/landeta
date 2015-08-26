CREATE TABLE gc_cur_team_stats_passing (
    id INTEGER PRIMARY KEY
  , gc_player_id TEXT
  , name TEXT
  , att INTEGER
  , cmp INTEGER
  , yds INTEGER
  , tds INTEGER
  , ints INTEGER
  , twopta INTEGER
  , twoptm INTEGER
  , gc_cur_team_id INTEGER
  , FOREIGN KEY (gc_cur_team_id) REFERENCES gc_cur_team (id)
)
;

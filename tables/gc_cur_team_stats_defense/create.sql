CREATE TABLE gc_cur_team_stats_defense (
    id INTEGER PRIMARY KEY
  , gc_player_id TEXT
  , name TEXT
  , tkl INTEGER
  , ast INTEGER
  , sk INTEGER
  , ffum INTEGER
  , ints INTEGER
  , gc_cur_team_id INTEGER
  , FOREIGN KEY (gc_cur_team_id) REFERENCES gc_cur_team (id)
)
;

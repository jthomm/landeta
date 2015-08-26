CREATE TABLE gc_cur_team_stats_fumble (
    id INTEGER PRIMARY KEY
  , gc_player_id TEXT
  , name TEXT
  , tot INTEGER
  , yds INTEGER
  , lost INTEGER
  , rcv INTEGER
  , trcv INTEGER
  , gc_cur_team_id INTEGER
  , FOREIGN KEY (gc_cur_team_id) REFERENCES gc_cur_team (id)
)
;

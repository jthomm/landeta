CREATE TABLE gc_cur_team_player (
    id INTEGER PRIMARY KEY
  , gc_player_id TEXT
  , esbid TEXT
  , fn TEXT
  , ln TEXT
  , hometown TEXT
  , bdate TEXT
  , age INTEGER
  , exp TEXT
  , pos TEXT
  , ht TEXT
  , wt INTEGER
  , college TEXT
  , team TEXT
  , uniformnumber INTEGER
  , gc_cur_team_id INTEGER
  , FOREIGN KEY (gc_cur_team_id) REFERENCES gc_cur_team (id)
)
;

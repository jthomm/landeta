CREATE TABLE gc_cur_team_stats_kicking (
    id INTEGER PRIMARY KEY
  , gc_player_id TEXT
  , name TEXT
  , totpfg INTEGER
  , fga INTEGER
  , fgm INTEGER
  , fgyds INTEGER
  , xptot INTEGER
  , xpa INTEGER
  , xpmade INTEGER
  , xpmissed INTEGER
  , xpb INTEGER
  , gc_cur_team_id INTEGER
  , FOREIGN KEY (gc_cur_team_id) REFERENCES gc_cur_team (id)
)
;

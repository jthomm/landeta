CREATE TABLE gc_cur_team_stats_team (
    id INTEGER PRIMARY KEY
  , totfd INTEGER
  , trnovr INTEGER
  , pyds INTEGER
  , ryds INTEGER
  , totyds INTEGER
  , pt INTEGER
  , ptyds INTEGER
  , ptavg INTEGER
  , pen INTEGER
  , penyds INTEGER
  , top TEXT
  , gc_cur_team_id INTEGER
  , FOREIGN KEY (gc_cur_team_id) REFERENCES gc_cur_team (id)
)
;

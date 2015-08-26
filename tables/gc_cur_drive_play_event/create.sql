CREATE TABLE gc_cur_drive_play_event (
    id INTEGER PRIMARY KEY
  , gc_player_id TEXT
  , playername TEXT
  , clubcode TEXT
  , yards INTEGER
  , statid INTEGER
  , sequence INTEGER
  , gc_cur_drive_play_id INTEGER
  , FOREIGN KEY (gc_cur_drive_play_id) REFERENCES gc_cur_drive_play (id)
)
;

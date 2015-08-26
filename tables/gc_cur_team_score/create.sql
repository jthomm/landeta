CREATE TABLE gc_cur_team_score (
    id INTEGER PRIMARY KEY
  , qtr TEXT
  , points INTEGER
  , gc_cur_team_id INTEGER
  , FOREIGN KEY (gc_cur_team_id) REFERENCES gc_cur_team (id)
)
;

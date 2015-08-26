def gc(game_id):
    return (game_id,)

def gc_game(gc_id, dct):
    return (dct['id'],
            dct['key'], #not "gc_game_key"
            dct['uri'],
            dct['gamebook'],
            dct['seasontype'],
            dct['week'],
            dct['cp'],
            dct['year'],
            dct['date'], #not "gc_game_date"
            dct['time'], #not "gc_game_time"
            dct['day'],
            dct['state'],
            gc_id,)

def gc_game_team(gc_game_id, abbr, dct):
    return (abbr,
            dct['fullname'],
            dct['link'],
            dct['standing'],
            gc_game_id,)

def gc_team(gc_id, ah, dct):
    return (ah,
            dct['standing'],
            dct['abbr'],
            gc_id,)

def gc_cur(gc_id, dct):
    return (1 if dct['redzone'] else 0,
            dct['rooftype'],
            dct['qtr'],
            dct['yl'],
            dct['clock'],
            dct['down'],
            dct['togo'],
            dct['posteam'],
            dct['stadium'],
            gc_id,)

def gc_cur_scrsummary(gc_cur_id, gc_play_id, dct):
    return (gc_play_id,
            dct['qtr'],
            dct['team'],
            dct['type'], #not "scr_type"
            dct['desc'], #not "descr"
            gc_cur_id,)

def gc_cur_scrsummary_player(gc_cur_scrsummary_id, gc_player_name, gc_player_id):
    return (gc_player_id,
            gc_player_name,
            gc_cur_scrsummary_id,)

def gc_cur_team(gc_cur_id, ah, dct):
    return (ah,
            dct['teamCode'],
            dct['abbr'],
            dct['fullName'],
            dct['comUrl'],
            dct['clubUrl'],
            dct['smsCode'],
            dct['color'],
            dct['teamColor'],
            dct['phone'],
            dct['standing'],
            dct['to'], #not "tout"
            gc_cur_id,)

def gc_cur_team_score(gc_cur_team_id, qtr, points):
    return (qtr,
            points,
            gc_cur_team_id,)

def gc_cur_team_stats_team(gc_cur_team_id, dct):
    return (dct['totfd'],
            dct['trnovr'],
            dct['pyds'],
            dct['ryds'],
            dct['totyds'],
            dct['pt'],
            dct['ptyds'],
            dct['ptavg'],
            dct['pen'],
            dct['penyds'],
            dct['top'],
            gc_cur_team_id,)

def gc_cur_team_stats_kickret(gc_cur_team_id, gc_player_id, dct):
    return (gc_player_id,
            dct['name'],
            dct['ret'],
            dct['avg'], #not "avrg"
            dct['lng'],
            dct['tds'],
            gc_cur_team_id,)

def gc_cur_team_stats_puntret(gc_cur_team_id, gc_player_id, dct):
    return (gc_player_id,
            dct['name'],
            dct['ret'],
            dct['avg'], #not "avrg"
            dct['lng'],
            dct['tds'],
            gc_cur_team_id,)

def gc_cur_team_stats_defense(gc_cur_team_id, gc_player_id, dct):
    return (gc_player_id,
            dct['name'],
            dct['tkl'],
            dct['ast'],
            dct['sk'],
            dct['ffum'],
            dct['int'], #not "ints"
            gc_cur_team_id,)

def gc_cur_team_stats_fumbles(gc_cur_team_id, gc_player_id, dct):
    return (gc_player_id,
            dct['name'],
            dct['tot'],
            dct['yds'],
            dct['lost'],
            dct['rcv'],
            dct['trcv'],
            gc_cur_team_id,)

def gc_cur_team_stats_kicking(gc_cur_team_id, gc_player_id, dct):
    return (gc_player_id,
            dct['name'],
            dct['totpfg'],
            dct['fga'],
            dct['fgm'],
            dct['fgyds'],
            dct['xptot'],
            dct['xpa'],
            dct['xpmade'],
            dct['xpmissed'],
            dct['xpb'],
            gc_cur_team_id,)

def gc_cur_team_stats_punting(gc_cur_team_id, gc_player_id, dct):
    return (gc_player_id,
            dct['name'],
            dct['pts'],
            dct['yds'],
            dct['avg'], #not "avrg"
            dct['lng'],
            dct['i20'],
            gc_cur_team_id,)

def gc_cur_team_stats_passing(gc_cur_team_id, gc_player_id, dct):
    return (gc_player_id,
            dct['name'],
            dct['att'],
            dct['cmp'],
            dct['yds'],
            dct['tds'],
            dct['ints'],
            dct['twopta'],
            dct['twoptm'],
            gc_cur_team_id,)

def gc_cur_team_stats_receiving(gc_cur_team_id, gc_player_id, dct):
    return (gc_player_id,
            dct.get('name', None),
            dct.get('rec', None),
            dct.get('yds', None),
            dct.get('tds', None),
            dct.get('lng', None),
            dct.get('lngtd', None),
            dct.get('twopta', None),
            dct.get('twoptm', None),
            gc_cur_team_id,)

def gc_cur_team_stats_rushing(gc_cur_team_id, gc_player_id, dct):
    return (gc_player_id,
            dct.get('name', None),
            dct.get('att', None),
            dct.get('yds', None),
            dct.get('tds', None),
            dct.get('lng', None),
            dct.get('lngtd', None),
            dct.get('twopta', None),
            dct.get('twoptm', None),
            gc_cur_team_id,)

def gc_cur_team_player(gc_cur_team_id, gc_player_id, dct):
    return (gc_player_id,
            dct['esbid'],
            dct['fn'],
            dct['ln'],
            dct['hometown'],
            dct['bdate'],
            dct['age'],
            dct['exp'],
            dct['pos'],
            dct['ht'],
            dct['wt'],
            dct['college'],
            dct['team'],
            dct['uniformNumber'],
            gc_cur_team_id,)

def gc_cur_drive(gc_cur_id, drive_num, dct):
    return (drive_num,
            None if 'redzone' not in dct else 1 if dct['redzone'] else 0,
            #1 if dct['redzone'] else 0,
            dct['postime'],
            dct['fds'],
            dct['result'],
            dct['numplays'],
            dct.get('qtr', None),
            dct['penyds'],
            dct['posteam'],
            dct['ydsgained'],
            dct['start']['yrdln'],
            dct['start']['team'],
            dct['start']['qtr'],
            dct['start']['time'],
            dct['end']['yrdln'],
            dct['end']['team'],
            dct['end']['qtr'],
            dct['end']['time'],
            gc_cur_id,)

def gc_cur_drive_play(gc_cur_drive_id, gc_play_id, dct):
    return (gc_play_id,
            dct['desc'], #not "descr"
            dct['posteam'],
            dct['qtr'],
            dct['time'],
            dct['down'],
            dct['ydstogo'],
            dct['yrdln'],
            dct['ydsnet'],
            dct['note'],
            dct['sp'],
            gc_cur_drive_id,)

def gc_cur_drive_play_event(gc_cur_drive_play_id, gc_player_id, dct):
    return (gc_player_id,
            dct['playerName'],
            dct['clubcode'],
            dct['yards'],
            dct['statId'],
            dct['sequence'],
            gc_cur_drive_play_id,)

from table import Table
import values



class GcCurDrivePlayEventInserter(object):

    def __init__(self, cursor, gc_cur_drive_play_id):
        self.cursor = cursor
        self.gc_cur_drive_play_id = gc_cur_drive_play_id
        self.table = Table('gc_cur_drive_play_event')

    def __call__(self, gc_player_id, dct):
        vals = values.gc_cur_drive_play_event(
            self.gc_cur_drive_play_id, gc_player_id, dct)
        self.table.insert(
            self.cursor,
            values.gc_cur_drive_play_event(
                self.gc_cur_drive_play_id,
                gc_player_id,
                dct))

class GcCurDrivePlayInserter(object):

    def __init__(self, cursor, gc_cur_drive_id):
        self.cursor = cursor
        self.gc_cur_drive_id = gc_cur_drive_id
        self.table = Table('gc_cur_drive_play')

    def __call__(self, gc_play_id, dct):
        gc_cur_drive_play_id = self.table.insert(
            self.cursor,
            values.gc_cur_drive_play(
                self.gc_cur_drive_id,
                gc_play_id,
                dct))
        event_inserter = GcCurDrivePlayEventInserter(
            self.cursor,
            gc_cur_drive_play_id)
        for gc_player_id, event_dcts in dct['players'].iteritems():
            for event_dct in event_dcts:
                event_inserter(gc_player_id, event_dct)

class GcCurDriveInserter(object):

    def __init__(self, cursor, gc_cur_id):
        self.cursor = cursor
        self.gc_cur_id = gc_cur_id
        self.table = Table('gc_cur_drive')

    def __call__(self, drive_num, dct):
        gc_cur_drive_id = self.table.insert(
            self.cursor,
            values.gc_cur_drive(
                self.gc_cur_id,
                drive_num,
                dct))
        play_inserter = GcCurDrivePlayInserter(self.cursor, gc_cur_drive_id)
        for gc_play_id, play_dct in dct['plays'].iteritems():
            play_inserter(gc_play_id, play_dct)

class GcCurTeamScoreInserter(object):

    def __init__(self, cursor, gc_cur_team_id):
        self.cursor = cursor
        self.gc_cur_team_id = gc_cur_team_id
        self.table = Table('gc_cur_team_score')

    def __call__(self, qtr, points):
        self.table.insert(
            self.cursor,
            values.gc_cur_team_score(
                self.gc_cur_team_id,
                qtr,
                points))

class GcCurTeamStatsTeamInserter(object):

    def __init__(self, cursor, gc_cur_team_id):
        self.cursor = cursor
        self.gc_cur_team_id = gc_cur_team_id
        self.table = Table('gc_cur_team_stats_team')

    def __call__(self, dct):
        self.table.insert(
            self.cursor,
            values.gc_cur_team_stats_team(
                self.gc_cur_team_id,
                dct))

class GcCurTeamStatsIndividualInserter(object):

    def __init__(self, cursor, gc_cur_team_id):
        self.cursor = cursor
        self.gc_cur_team_id = gc_cur_team_id

    def __call__(self, category, player_id, dct):
        table_name = 'gc_cur_team_stats_{0}'.format(category)
        table = Table(table_name)
        table.insert(
            self.cursor,
            getattr(values, table_name)(
                self.gc_cur_team_id,
                player_id,
                dct))

class GcCurTeamPlayerInserter(object):

    def __init__(self, cursor, gc_cur_team_id):
        self.cursor = cursor
        self.gc_cur_team_id = gc_cur_team_id
        self.table = Table('gc_cur_team_player')

    def __call__(self, gc_player_id, dct):
        self.table.insert(
            self.cursor,
            values.gc_cur_team_player(
                self.gc_cur_team_id,
                gc_player_id,
                dct))

class GcCurTeamInserter(object):

    def __init__(self, cursor, gc_cur_id):
        self.cursor = cursor
        self.gc_cur_id = gc_cur_id
        self.table = Table('gc_cur_team')

    def __call__(self, ah, dct):
        gc_cur_team_id = self.table.insert(
            self.cursor,
            values.gc_cur_team(
                self.gc_cur_id,
                ah,
                dct))
        # Insert score
        score_inserter = GcCurTeamScoreInserter(
            self.cursor, gc_cur_team_id)
        for qtr, points in dct['score'].iteritems():
            score_inserter(qtr, points)
        # Insert team players
        team_player_inserter = GcCurTeamPlayerInserter(
            self.cursor, gc_cur_team_id)
        for gc_player_id, gc_player_dct in dct['players'].iteritems():
            team_player_inserter(gc_player_id, gc_player_dct)
        # Insert team stats
        stats_team_inserter = GcCurTeamStatsTeamInserter(
            self.cursor, gc_cur_team_id)
        stats_team_inserter(dct['stats']['team'])
        # Insert individual stats
        stats_individual_inserter = GcCurTeamStatsIndividualInserter(
            self.cursor, gc_cur_team_id)
        for category in ('kickret', 'puntret', 'defense', 'fumbles', \
                         'kicking', 'punting', 'passing', 'receiving', \
                         'rushing',):
            if category not in dct['stats']:
                # Some categories aren't in every team dict in every game?
                continue
            for player_id, category_dct in dct['stats'][category].iteritems():
                stats_individual_inserter(
                    category, player_id, category_dct)

class GcCurScrsummaryPlayerInserter(object):

    def __init__(self, cursor, gc_cur_scrsummary_id):
        self.cursor = cursor
        self.gc_cur_scrsummary_id = gc_cur_scrsummary_id
        self.table = Table('gc_cur_scrsummary_player')

    def __call__(self, gc_player_name, gc_player_id):
        self.table.insert(
            self.cursor,
            values.gc_cur_scrsummary_player(
                self.gc_cur_scrsummary_id,
                gc_player_name,
                gc_player_id))

class GcCurScrsummaryInserter(object):

    def __init__(self, cursor, gc_cur_id):
        self.cursor = cursor
        self.gc_cur_id = gc_cur_id
        self.table = Table('gc_cur_scrsummary')

    def __call__(self, gc_play_id, dct):
        gc_cur_scrsummary_id = self.table.insert(
            self.cursor,
            values.gc_cur_scrsummary(
                self.gc_cur_id,
                gc_play_id,
                dct))
        scrsummary_player_inserter = GcCurScrsummaryPlayerInserter(
            self.cursor, gc_cur_scrsummary_id)
        for gc_player_name, gc_player_id in dct['players'].iteritems():
            scrsummary_player_inserter(gc_player_name, gc_player_id)

class GcCurInserter(object):

    def __init__(self, cursor, gc_id):
        self.cursor = cursor
        self.gc_id = gc_id
        self.table = Table('gc_cur')

    def __call__(self, dct):
        gc_cur_id = self.table.insert(
            self.cursor,
            values.gc_cur(self.gc_id, dct))
        # Insert drives
        drive_inserter = GcCurDriveInserter(self.cursor, gc_cur_id)
        for drive_num, drive_dct in dct['drives'].iteritems():
            # Most keys in `dct['drives']` will be a drive number and their 
            # values will be a drive dictionary.  One exception:  the key 
            # 'crntdrv', which has an integer value.  Skip this key/value pair.
            if drive_num != 'crntdrv':
                drive_inserter(drive_num, drive_dct)
        # Insert teams
        team_inserter = GcCurTeamInserter(self.cursor, gc_cur_id)
        for ah in ('away', 'home',):
            team_inserter(ah, dct[ah])
        # Insert score summary
        scrsummary_inserter = GcCurScrsummaryInserter(self.cursor, gc_cur_id)
        for gc_play_id, scrsummary_dct in dct['scrsummary'].iteritems():
            scrsummary_inserter(gc_play_id, scrsummary_dct)

class GcGameTeamInserter(object):

    def __init__(self, cursor, gc_game_id):
        self.cursor = cursor
        self.gc_game_id = gc_game_id
        self.table = Table('gc_game_team')

    def __call__(self, abbr, dct):
        self.table.insert(
            self.cursor,
            values.gc_game_team(self.gc_game_id, abbr, dct))

class GcGameInserter(object):

    def __init__(self, cursor, gc_id):
        self.cursor = cursor
        self.gc_id = gc_id
        self.table = Table('gc_game')

    def __call__(self, game_id, dct):
        gc_game_id = self.table.insert(
            self.cursor,
            values.gc_game(game_id, dct))
        game_team_inserter = GcGameTeamInserter(cursor, gc_game_id)
        for abbr, game_team_dct in dct['teams'].iteritems():
            game_team_inserter(abbr, game_team_dct)

class GcTeamInserter(object):

    def __init__(self, cursor, gc_id):
        self.cursor = cursor
        self.gc_id = gc_id
        self.table = Table('gc_team')

    def __call__(self, dct):
        for ah in ('away', 'home',):
            self.table.insert(
                self.cursor,
                values.gc_team(self.gc_id, ah, dct[ah]))

class GcInserter(object):

    def __init__(self, cursor, game_id):
        self.cursor = cursor
        self.game_id = game_id
        self.table = Table('gc')

    def __call__(self, dct):
        gc_id = self.table.insert(
            self.cursor,
            values.gc(self.game_id))
        gc_game_inserter = GcGameInserter(self.cursor, gc_id)
        gc_game_inserter(self.game_id, dct['game'])
        gc_team_inserter = GcTeamInserter(self.cursor, gc_id)
        gc_team_inserter(dct['teams'])
        gc_cur_inserter = GcCurInserter(self.cursor, gc_id)
        gc_cur_inserter(dct['current'][self.game_id])



table_names = ('gc',
               'gc_game',
               'gc_game_team',
               'gc_team',
               'gc_cur',
               'gc_cur_scrsummary',
               'gc_cur_scrsummary_player',
               'gc_cur_team',
               'gc_cur_team_score',
               'gc_cur_team_stats_team',
               'gc_cur_team_stats_kickret',
               'gc_cur_team_stats_puntret',
               'gc_cur_team_stats_defense',
               'gc_cur_team_stats_fumbles',
               'gc_cur_team_stats_kicking',
               'gc_cur_team_stats_punting',
               'gc_cur_team_stats_passing',
               'gc_cur_team_stats_receiving',
               'gc_cur_team_stats_rushing',
               'gc_cur_team_player',
               'gc_cur_drive',
               'gc_cur_drive_play',
               'gc_cur_drive_play_event',)



def database_is_empty(cursor):
    results = cursor.execute('SELECT COUNT (*) FROM sqlite_master').fetchall()
    return results[0][0] == 0

def create_tables(cursor):
    for table_name in table_names:
        table = Table(table_name)
        table.create(cursor)

def insert_into_tables(cursor, game_id, dct):
    gc_inserter = GcInserter(cursor, game_id)
    gc_inserter(dct)

def make_argument_parser():
    argument_parser = argparse.ArgumentParser(
        description='Inserter data for a given game')
    argument_parser.add_argument(
        '-d', '--database', help='path to the SQLite database file')
    argument_parser.add_argument(
        '-f', '--filename', help='path to the Game Center .json file')
    argument_parser.add_argument(
        '-g', '--gameid', help="Game Center ID of the game (e.g. '2014092800')")
    return argument_parser



if __name__ == '__main__':
    import sqlite3
    try:
        import simplejson as json
    except ImportError:
        import json
    import argparse
    # Make the object that parses command line arguments
    argument_parser = make_argument_parser()
    args = argument_parser.parse_args()
    # Read the game data from a json file and de-serialize it into `dct`
    json_data = ''
    with open(args.filename, 'rb') as f:
        json_data = f.read()
    dct = json.loads(json_data)
    # Enter a connection to the database
    with sqlite3.connect(args.database) as connection:
        cursor = connection.cursor()
        # If tables aren't already there, create them
        if database_is_empty(cursor):
            print 'No objects found in database -- creating tables first...'
            create_tables(cursor)
        try:
            # Insert the game
            game_id = args.gameid
            print 'Inserting {}'.format(game_id)
            insert_into_tables(cursor, game_id, dct)
        except sqlite3.OperationalError as e:
            print 'There was an issue executing one or more database inserts'
            raise e
        else:
            # If no errors, commit
            connection.commit()

from psycopg import Cursor
from utils import parse_int, parse_float

def populate_common_player_info(cur: Cursor, rows: list[dict[str,str]]):
    for row in rows:
        nba_player = (
            row['person_id'],
            row['display_first_last'],
            row['height'],
            parse_int(row['weight']),
            row['team_name'],
            row['position'],
            row['jersey']
        )
        cur.execute("""
            insert into common_players_info(person_id,display_first_last, height, weight, team_name, position, jersey)
            values(%s, %s, %s,%s, %s, %s,%s)
            on conflict do nothing
            """, nba_player)
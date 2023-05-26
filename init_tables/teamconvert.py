from psycopg import Cursor
from utils import parse_int, parse_float

def populate_team_convert(cur: Cursor, rows: list[dict[str,str]]):
    for row in rows:
        nba_player = (
            row['team_name'],
            row['team_abr']
        )
        cur.execute("""
            insert into teamconvert(team_name, team_abr)
            values(%s, %s)
            on conflict do nothing
            """, nba_player)
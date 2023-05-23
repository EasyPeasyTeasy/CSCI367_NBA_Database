
from psycopg import Cursor
from utils import parse_int

def populate_team_details(cur: Cursor, rows: list[dict[str,str]]):
    for row in rows:
        nba_player = (
            parse_int(row['team_id']),
            row['headcoach']
        )
        cur.execute("""
            insert into team_details(team_id, headcoach)
            values(%s, %s)
            on conflict do nothing
            """, nba_player)
        
        
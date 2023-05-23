from psycopg import Cursor
from utils import parse_int, parse_boolean

def populate_player(cur: Cursor, rows: list[dict[str,str]]):
    for row in rows:
        nba_player = (
            parse_int(row['id']),
            row['full_name'],
            parse_boolean(row['is_active'])
        )
        cur.execute("""
            insert into player(id, full_name, is_active)
            values(%s, %s, %s)
            on conflict do nothing
            """, nba_player)
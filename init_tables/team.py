from psycopg import Cursor
from utils import parse_int, parse_float

def populate_team(cur: Cursor, rows: list[dict[str,str]]):
    for row in rows:
        nba_team = (
            parse_int(row['id']),
            row['full_name'],
            row['city'],
            row['state'],
            parse_float(row['year_founded']),
            row['abbreviation']
        )
        cur.execute("""
            insert into team(id, full_name, city, state, year_founded, abbreviation)
            values(%s, %s, %s, %s, %s, %s)
            on conflict do nothing
            """, nba_team)
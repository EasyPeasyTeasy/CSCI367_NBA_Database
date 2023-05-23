from psycopg import Cursor
from utils import parse_int, parse_float

def populate_NBA_data_processed(cur: Cursor, rows: list[dict[str,str]]):
    for row in rows:
        nba_player = (
            row['Player'],
            row['Pos'],
            parse_int(row['Age']),
            row['Tm'],
            parse_float(row['FG%']),
            parse_float(row['3P%']),
            parse_float(row['2P%']),
            parse_float(row['FT%']),
            parse_float(row['AST']),
            parse_float(row['STL']),
            parse_float(row['BLK']),
            parse_float(row['PTS'])
        )
        cur.execute("""
            insert into NBA_data_processed(player,pos,age,Tm,FG,threeP,twoP,FT, AST, STL, BLK, Pts)
            values(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s)
            on conflict do nothing
            """, nba_player)
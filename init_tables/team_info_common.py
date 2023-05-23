from psycopg import Cursor
from utils import parse_int, parse_boolean

def populate_team_info_common(cur: Cursor, rows: list[dict[str,str]]):
    for row in rows:
        nba_player = (
            parse_int(row['team_id']),
            row['team_name'],
            row['season_year'],
            row['team_conference'],
            row['team_division'],
            parse_int(row['conf_rank']),
            parse_int(row['div_rank']),
            parse_int(row['pts_rank']),
            parse_int(row['reb_rank']),
            parse_int(row['ast_rank'])
        )
        cur.execute("""
            insert into teams_info_common(team_id, team_name, season_year, team_conference, team_division, conf_rank, div_rank, pts_rank, reb_rank, ast_rank)
            values(%s, %s, %s, %s,%s, %s, %s,%s, %s, %s)
            on conflict do nothing
            """, nba_player)
from psycopg2.extensions import cursor

def search_team(cur: cursor, 
                  season_year_contains: str,
                  team_name_contains: str,
                  team_conference_contains: str,
                  team_division_contains: str,
                  sort_dir: str,
                  offset:int) -> list[dict[str,str]]:
    
    cur.execute(
        f"""
        SELECT season_year,
            team_name,
            team_conference,
            team_division,
            conf_rank,
            div_rank,
            pts_rank,
            reb_rank,
            ast_rank
        FROM teams_info_common
        WHERE LOWER(season_year) LIKE LOWER(%(season_year_param)s)
            AND LOWER(team_name) LIKE LOWER(%(team_name_param)s)
            AND LOWER(team_conference) LIKE LOWER(%(team_conference_param)s)
            AND LOWER(team_division) LIKE LOWER(%(team_division_param)s)
        order by conf_rank {sort_dir}
        limit 25
        offset {offset}
        """,
        {
            'season_year_param': f"%{season_year_contains or ''}%",
            'team_name_param': f"%{team_name_contains or ''}%",
            'team_conference_param': f"%{team_conference_contains or ''}%",
            'team_division_param': f"%{team_division_contains or ''}%"
        }
    )
    return list(cur)

def count_team(cur: cursor, 
                  season_year_contains: str,
                  team_name_contains: str,
                  team_conference_contains: str,
                  team_division_contains: str) -> list[dict[str,str]]:
    
    cur.execute(
        f"""
        SELECT count(*)
        FROM teams_info_common
        WHERE LOWER(season_year) LIKE LOWER(%(season_year_param)s)
            AND LOWER(team_name) LIKE LOWER(%(team_name_param)s)
            AND LOWER(team_conference) LIKE LOWER(%(team_conference_param)s)
            AND LOWER(team_division) LIKE LOWER(%(team_division_param)s)
        """,
        {
            'season_year_param': f"%{season_year_contains or ''}%",
            'team_name_param': f"%{team_name_contains or ''}%",
            'team_conference_param': f"%{team_conference_contains or ''}%",
            'team_division_param': f"%{team_division_contains or ''}%"
        }
    )
    return cur.fetchone()['count']
        

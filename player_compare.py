from psycopg2.extensions import cursor

def compare_player(cur: cursor, 
                  name_1_contains: str,
                  name_2_contains: str,
                  name_3_contains: str,
                  team_1_contains: str,
                  team_2_contains: str,
                  team_3_contains: str) -> list[dict[str,str]]:
    
    cur.execute(
        f"""
        SELECT *
        FROM nba_data_processed
        LEFT JOIN teamconvert ON LOWER(Tm) = LOWER(team_abr)
        WHERE (LOWER(player) LIKE LOWER(%(name_1_param)s)
            AND LOWER(team_name) LIKE LOWER(%(team_1_param)s))
        OR (LOWER(player) LIKE LOWER(%(name_2_param)s)
            AND LOWER(team_name) LIKE LOWER(%(team_2_param)s))
        OR (LOWER(player) LIKE LOWER(%(name_3_param)s)
            AND LOWER(team_name) LIKE LOWER(%(team_3_param)s))
            
        """,
        {
            'name_1_param': f"%{name_1_contains or ''}%",
            'team_1_param': f"%{team_1_contains or ''}%",
            'name_2_param': f"%{name_2_contains or ''}%",
            'team_2_param': f"%{team_2_contains or ''}%",
            'name_3_param': f"%{name_3_contains or ''}%",
            'team_3_param': f"%{team_3_contains or ''}%",
        }
    )
    return list(cur)

def count_player(cur: cursor, 
                  player_name_contains: str,
                  position_contains: str,
                  team_name_contains: str, 
                  jersey:str) -> list[dict[str,str]]:
    
    cur.execute(
        f"""
        SELECT count(*)
        FROM common_players_info
        WHERE LOWER(display_first_last) LIKE LOWER(%(player_name_param)s)
            AND LOWER(position) LIKE LOWER(%(position_param)s)
            AND LOWER(team_name) LIKE LOWER(%(team_name_param)s)
            AND LOWER(jersey) LIKE LOWER(%(jersey_param)s)
        """,
        {
            'player_name_param': f"%{player_name_contains or ''}%",
            'position_param': f"%{position_contains or ''}%",
            'team_name_param': f"%{team_name_contains or ''}%",
            'jersey_param': f"%{jersey or ''}%",
        }
    )
    return cur.fetchone()['count']
        

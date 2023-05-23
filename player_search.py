from psycopg2.extensions import cursor

def search_player(cur: cursor, 
                  player_name_contains: str,
                  position_contains: str,
                  team_name_contains: str,
                  jersey:str,
                  offset:int) -> list[dict[str,str]]:
    
    cur.execute(
        f"""
        SELECT display_first_last,
            position,
            team_name,
            jersey
        FROM common_players_info
        WHERE LOWER(display_first_last) LIKE LOWER(%(player_name_param)s)
            AND LOWER(position) LIKE LOWER(%(position_param)s)
            AND LOWER(team_name) LIKE LOWER(%(team_name_param)s)
            AND LOWER(jersey) LIKE LOWER(%(jersey_param)s)
        limit 25
        offset {offset}
        """,
        {
            'player_name_param': f"%{player_name_contains or ''}%",
            'position_param': f"%{position_contains or ''}%",
            'team_name_param': f"%{team_name_contains or ''}%",
            'jersey_param': f"%{jersey or ''}%",
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
        

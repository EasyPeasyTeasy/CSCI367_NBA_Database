create table if not exists teams_info_common (
    team_id int primary key references team(id), 
    team_name text,
    season_year text,
    team_conference text,
    team_division text,
    conf_rank int,
    div_rank int,
    pts_rank int, 
    reb_rank int, 
    ast_rank int
)
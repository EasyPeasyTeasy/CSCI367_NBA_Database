create table if not exists common_players_info(
    person_id int primary key references player(id), 
    display_first_last text,
    height text,
    weight int,
    team_name text,
    position text,
    jersey text
)
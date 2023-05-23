create table if not exists team_details(
    team_id int primary key references team(id),
    headcoach text
)
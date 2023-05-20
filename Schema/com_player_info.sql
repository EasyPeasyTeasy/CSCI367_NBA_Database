create table if not exists cpi (
    /*
    example:
        person_id,first_name,last_name,display_first_last,display_last_comma_first,display_fi_last,player_slug,birthdate,
        school,country,last_affiliation,height,weight,season_exp,jersey,position,rosterstatus,games_played_current_season_flag,
        team_id,team_name,team_abbreviation,team_code,team_city,playercode,from_year,to_year,dleague_flag,nba_flag,
        games_played_flag,draft_year,draft_round,draft_number,greatest_75_flag
        
        51,Mahmoud,Abdul-Rauf,Mahmoud Abdul-Rauf,"Abdul-Rauf, Mahmoud",M. Abdul-Rauf,mahmoud-abdul-rauf,1969-03-09 00:00:00,
        Louisiana State,USA,Louisiana State/USA,6-1,162,9.0,1,Guard,Inactive,N,
        1610612743,Nuggets,DEN,nuggets,Denver,mahmoud_abdul-rauf,1990.0,2000.0,N,Y,
        Y,1990,1,3,N
 */

    person_id int primary key,
    first_name text not null,
    last_name text not null,
    birthdate date not null,
    school text,
    country text not null,
    height text not null,
    weight int not null,
    


)
    
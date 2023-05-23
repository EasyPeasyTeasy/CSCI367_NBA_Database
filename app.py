import psycopg2
from flask import Flask, render_template, request
from psycopg2.extras import RealDictCursor
from player_search import search_player, count_player
from team_search import search_team, count_team
import math

SORT_DIRS = {"asc", "desc"}

conn = psycopg2.connect(
    "host=db dbname=postgres user=postgres password=postgres",
    cursor_factory=RealDictCursor)
app = Flask(__name__)

#@app.route('/hello')
#def hello_world():
#    return "Hello, World!"

@app.route('/')
def home():
    return render_template('nbatipoff.html')

@app.route('/player')
def player():
    with conn.cursor() as curr:
        player_name_contains = request.args.get("display_first_last", "")
        position_contains = request.args.get("position", "")
        team_name_contains = request.args.get("team_name", "")
        jersey = request.args.get("jersey","")
        limit=  25
        page_number = request.args.get("pagenumber", 1)
        total_results = count_player(curr, player_name_contains, position_contains, team_name_contains, jersey)
        offset = (int(page_number)-1) * 25
        total_pages = math.ceil(int(total_results) / 25)
        user_search = search_player(curr, player_name_contains, position_contains, team_name_contains, jersey, offset)
        return render_template('playertipoff.html',
                            player_name_contains = player_name_contains,
                            position_contains = position_contains,
                            team_name_contains = team_name_contains,
                            jersey = jersey,
                            total_pages = total_pages,
                            page_number = page_number,
                            user_search = user_search)

@app.route('/teams')
def teams():
    with conn.cursor() as curr:
        season_year_contains = request.args.get("season_year", "")
        team_name_contains = request.args.get("team_name", "")
        team_conference_contains = request.args.get("team_conference", "")
        team_division_contains = request.args.get("team_division", "")
        sort_dir = request.args.get("sort_dir", "asc")
        limit=  25
        page_number = request.args.get("pagenumber", 1)
        total_results = count_team(curr, season_year_contains,  team_name_contains,team_conference_contains, team_division_contains)
        offset = (int(page_number)-1) * 25
        total_pages = math.ceil(int(total_results) / 25)
        user_search = search_team(curr, season_year_contains, team_name_contains, team_conference_contains, team_division_contains, sort_dir, offset)

        if sort_dir not in SORT_DIRS:
            sort_dir = "asc"

        def get_sort_dir():
            return "desc" if sort_dir == "asc" else "asc"

        return render_template('teamtipoff.html',
                            season_year_contains = season_year_contains,
                            team_name_contains = team_name_contains,
                            team_conference_contains  =  team_conference_contains, 
                            team_division_contains = team_division_contains,
                            total_pages = total_pages,
                            page_number = page_number,
                            user_search = user_search,
                            get_sort_dir = get_sort_dir)


@app.route('/compare')
def compare():
    return render_template('comparetipoff.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
#app.run(host='0.0.0.0', port=105)

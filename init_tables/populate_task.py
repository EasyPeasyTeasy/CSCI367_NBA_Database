
import csv

from typing import Callable, NamedTuple

from psycopg2.extensions import connection

from player import populate_player

from team import populate_team

from team_details import populate_team_details

from team_info_common import populate_team_info_common

from NBA_date_processed import populate_NBA_data_processed

from common_player_info import populate_common_player_info

from teamconvert import populate_team_convert




class PopulateTask(NamedTuple):
    create_table_file_path: str
    data_file_path: str
    populate_fn: Callable[[list[dict[str, str]]], None]


def populate(task: PopulateTask, conn: connection) -> None:
    with conn.cursor() as cur:
        with open(task.create_table_file_path, encoding="utf8") as schema_file:
            cur.execute(schema_file.read())
        print(f"executed schema file {task.create_table_file_path}")
        with open(task.data_file_path, encoding="utf8") as csv_file:
            rows = list(csv.DictReader(csv_file))
            task.populate_fn(cur, rows)
        print(f"processed {task.data_file_path}")


POPULATE_TASKS: list[PopulateTask] = [
     PopulateTask("../schema/NBA_data_processed.sql",
                 "../Data/csv_data/nba_data_processed.csv", populate_NBA_data_processed),
    PopulateTask("../schema/player.sql",
                 "../Data/csv_data/player.csv", populate_player),
    PopulateTask("../schema/team.sql",
                 "../Data/csv_data/team.csv", populate_team),
    PopulateTask("../schema/team_details.sql",
                 "../Data/csv_data/team_details.csv", populate_team_details),
    PopulateTask("../schema/team_info_common.sql",
                 "../Data/csv_data/team_info_common.csv", populate_team_info_common),
   PopulateTask("../schema/common_player_info.sql",
                 "../Data/csv_data/common_player_info.csv", populate_common_player_info),
    PopulateTask("../schema/teamconvert.sql",
                 "../Data/csv_data/teamconvert.csv", populate_team_convert)
   
    
]
import psycopg
import os
from helpers import print_color
from crud_operations import *
from create_operations import *


def main():
    # schema design link: https://dbdiagram.io/d/6ac76c22a5ab2804191e2004
    connection_string = os.getenv('ALEKS_DB_URL')

    with psycopg.connect(connection_string) as conn:
        print('PostgreSQL DB Connected')

        create_activity_log_table(conn)
        create_user_table(conn)
        create_area_table(conn)
        create_location_table(conn)
        create_activity_type_table(conn)
        create_activity_table(conn)
        create_sleep_table(conn)
        create_light_measurement_table(conn)
        create_goal_table(conn)
        create_app_session_table(conn)

        print_color('Tables Created', "green")


if __name__ == "__main__":
    main()
import psycopg
import os
from helpers import print_color
from create_operations import create_all_tables


def main():
    # schema design link: https://dbdiagram.io/d/6ac76c22a5ab2804191e2004
    connection_string = os.getenv('ALEKS_DB_URL')

    with psycopg.connect(connection_string) as conn:
        print('PostgreSQL DB Connected')

        create_all_tables(conn)

        print_color('Tables Created', "green")


if __name__ == "__main__":
    main()
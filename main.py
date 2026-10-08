import psycopg
import os
from helpers import print_color
from crud_operations import *


def main():
    # schema design link: https://dbdiagram.io/d/6ac76c22a5ab2804191e2004
    connection_string = os.getenv('ALEKS_DB_URL')

    with psycopg.connect(connection_string) as conn:
        print('PostgreSQL DB Connected')

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


def create_user_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
        """)
    conn.commit()


def create_area_table(conn):
    with conn.cursor() as cur:
        # NUMERIC(9,2) means NUMERIC(no. of signifigant figures in the number, the number of digits after the decimal)
        # docs link: https://www.postgresql.org/docs/9.6/datatype-numeric.html
        cur.execute("""
            CREATE TABLE IF NOT EXISTS areas (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                latitude NUMERIC(9, 6) NOT NULL,
                longitude NUMERIC(9, 6) NOT NULL,
                radius_meters NUMERIC(10, 2) NOT NULL
            );
        """)
    conn.commit()


def create_location_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS locations (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id),
                area_id INTEGER REFERENCES areas(id),
                latitude NUMERIC(9, 6) NOT NULL,
                longitude NUMERIC(9, 6) NOT NULL,
                timestamp TIMESTAMP NOT NULL
            );
        """)
    conn.commit()


def create_activity_type_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS activity_types (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                category VARCHAR(100)
            );
        """)
    conn.commit()


def create_activity_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS activities (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id),
                activity_type_id INTEGER NOT NULL REFERENCES activity_types(id),
                start_time TIMESTAMP NOT NULL,
                end_time TIMESTAMP
            );
        """)
    conn.commit()


def create_sleep_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS sleep (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id),
                sleep_start_time TIMESTAMP NOT NULL,
                sleep_end_time TIMESTAMP
            );
        """)
    conn.commit()


def create_light_measurement_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS light_measurements (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id),
                sensor_type VARCHAR(100) NOT NULL,
                value NUMERIC(10, 2) NOT NULL,
                unit VARCHAR(50) NOT NULL,
                timestamp TIMESTAMP NOT NULL
            );
        """)
    conn.commit()


def create_goal_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS goals (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id),
                name VARCHAR(100) NOT NULL,
                target_duration_minutes INTEGER NOT NULL,
                period VARCHAR(50) NOT NULL
            );
        """)
    conn.commit()


def create_app_session_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS app_sessions (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id),
                start_time TIMESTAMP NOT NULL,
                end_time TIMESTAMP
            );
        """)
    conn.commit()


if __name__ == "__main__":
    main()
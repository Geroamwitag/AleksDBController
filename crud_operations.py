class CRUD:
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()

    #
    # CREATE
    #
    def create_table(self, conn):
        with conn.cursor() as cur:

            cur.execute("""
                CREATE TABLE IF NOT EXISTS FIRST_TABLE (
                    id SERIAL PRIMARY KEY,
                    COLUMN1 VARCHAR(100) NOT NULL,
                    COLUMN2 VARCHAR(255) UNIQUE NOT NULL,
                    COLUMN3 INTEGER
                );
            """)
        conn.commit()


    def insert_into(self, conn, table_name):
        self.cur.execute(
            # insert into query
            ...
        )

    #
    # READ
    #
    def read_table(self, conn, table_name: str):
        self.cur.execute(
            # read query
            ...
        )


    #
    # UPDATE
    #
    def update_table(self, conn):
        self.cur.execute(
            # update query
            ...
        )

    #
    # DELETE
    #
    def delete_from_table(self, conn, table_name: str):
        self.cur.execute(
            # delete from query
            ...
        )
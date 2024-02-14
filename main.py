import sqlite3
from contextlib import contextmanager
from faker import Faker

DATABASE = './college.db'
SQL_PATH = './sql/'


@contextmanager
def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()


def execute_script(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.executescript(create_table_sql)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def create_tables(conn):
    try:
        with open(f"{SQL_PATH}create_all_tables.sql", "r") as f:
            sql = f.read()
        execute_script(conn, sql)
        return 0
    except Exception as e:
        print(f"Error: An exception occurred - {type(e).__name__}: {e}")
        return -1

def generate_fake_data(conn):
    fake = Faker()

    # for table: Teachers
    for _ in range(5):
        first_name = fake.first_name()
        last_name = fake.last_name()
        insert_sql = f"INSERT INTO Teachers (FirstName, LastName) VALUES ('{first_name}', '{last_name}')"
        execute_script(conn, insert_sql)

if __name__ == '__main__':

    with create_connection(DATABASE) as conn:
        if conn is not None:
            create_tables(conn)
            generate_fake_data(conn)
        else:
            print("Error: Cannot create the database connection.")



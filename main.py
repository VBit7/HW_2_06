import sqlite3
from contextlib import contextmanager

DATABASE = './college.db'


@contextmanager
def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def create_project_tables


if __name__ == '__main__':
    sql_create_table_student = """
        CREATE TABLE IF NOT EXISTS Student (
            StudentId integer PRIMARY KEY,
            FirstName String(30),
            SecondName String(30),
            GroupId integer
        );
    """

    with create_connection(DATABASE) as conn:
        if conn is not None:
            # create_table(conn, sql_create_table_group)
            create_table(conn, sql_create_table_student)
            # create_table(conn, sql_create_table_teacher)
            # create_table(conn, sql_create_table_subject)
            # create_table(conn, sql_create_table_grade)
        else:
            print("Error! Cannot create the database connection.")



import sqlite3
from contextlib import contextmanager
from faker import Faker

DATABASE = './college.db'
SQL_PATH = './sql/'
NEW_TABLES = True

NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 8
NUMBER_GROUPS = 3
NUMBER_STUDENTS = 50
NUMBER_GRADES = 20


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


def manage_db(conn, filename):
    try:
        with open(f"{SQL_PATH}{filename}", "r") as f:
            sql = f.read()
        execute_script(conn, sql)
        return 0
    except Exception as e:
        print(f"Error: An exception occurred - {type(e).__name__}: {e}")
        return -1


def generate_fake_data(number_teachers, number_subjects, number_groups, number_students, number_grades):
    fake_teachers = []
    fake_subjects = []
    fake_groups = []
    fake_students = []
    fake_grades = []

    fake_data = Faker()

    for _ in range(number_teachers):
        # fake_teachers.append(fake_data.first_name(), fake_data.last_name())
        fake_teachers.append(fake_data.last_name())

    return fake_teachers, fake_subjects, fake_groups, fake_students, fake_grades


def prepare_data(teachers, subjects, groups, students, grades):
    for_teachers = []
    for_subjects = []
    for_groups = []
    for_students = []
    for_grades = []

    for teacher in teachers:
        for_teachers.append((teacher, ))

    return for_teachers, for_subjects, for_groups, for_students, for_grades


def insert_data_to_bd(teachers, subjects, groups, students, grades):

    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        sql_to_teachers = "INSERT INTO Teachers (LastName) VALUES (?)"
        cur.executemany(sql_to_teachers, teachers)

        con.commit()


# def generate_fake_data(conn):
#     fake = Faker()
#
#     # for table: Teachers
#     for _ in range(5):
#         first_name = fake.first_name()
#         last_name = fake.last_name()
#         insert_sql = f"INSERT INTO Teachers (FirstName, LastName) VALUES ('{first_name}', '{last_name}')"
#         execute_script(conn, insert_sql)


if __name__ == '__main__':

    with create_connection(DATABASE) as conn:
        if conn is not None:
            if NEW_TABLES:
                manage_db(conn, 'drop_all_tables.sql')
            manage_db(conn, 'create_all_tables.sql')
            # generate_fake_data(conn)

            teachers, subjects, groups, students, grades = prepare_data(*generate_fake_data(
                NUMBER_TEACHERS, NUMBER_SUBJECTS, NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_GRADES)
            )

            print(teachers)

            # insert_data_to_bd(teachers, subjects, groups, students, grades)


        else:
            print("Error: Cannot create the database connection.")



import datetime
import os
import sqlite3
from contextlib import contextmanager
from random import randint, choice
from faker import Faker

from tabulate import tabulate

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


def insert_script(conn, insert_sql, data_sql):
    try:
        c = conn.cursor()
        c.executemany(insert_sql, data_sql)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_script(conn, select_sql):
    try:
        c = conn.cursor()
        c.execute(select_sql)
        return c.fetchall(), c
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
    fake_dates = []
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)

    fake_data = Faker()

    for _ in range(number_teachers):
        fake_teachers.append([fake_data.first_name(), fake_data.last_name()])

    for _ in range(number_subjects):
        fake_subjects.append(fake_data.job())

    for _ in range(number_groups):
        fake_groups.append(fake_data.company())

    for _ in range(number_students):
        fake_students.append([fake_data.first_name(), fake_data.last_name()])

    for _ in range(1, number_students * number_subjects * number_grades + 1):
        fake_dates.append(fake_data.date_time_between(start_date=start_date, end_date=end_date))

    return fake_teachers, fake_subjects, fake_groups, fake_students, fake_dates


def prepare_data(teachers, subjects, groups, students, fake_dates):
    for_teachers = []
    for_subjects = []
    for_groups = []
    for_students = []
    for_grades = []

    for first_name, last_name in teachers:
        for_teachers.append((first_name, last_name))

    for subject_name in subjects:
        for_subjects.append((subject_name, randint(1, NUMBER_TEACHERS)))

    for group in groups:
          for_groups.append((group, ))

    for first_name, last_name in students:
        for_students.append((first_name, last_name, randint(1, NUMBER_GROUPS)))

    for fdate in fake_dates:
        for_grades.append((randint(1, NUMBER_STUDENTS), randint(1, NUMBER_SUBJECTS), randint(50, 100), fdate.isoformat()))

    return for_teachers, for_subjects, for_groups, for_students, for_grades


def insert_data_to_bd(conn, teachers, subjects, groups, students, grades):

    sql_to_teachers = "INSERT INTO Teachers (FirstName, LastName) VALUES (?, ?)"
    insert_script(conn, sql_to_teachers, teachers)

    sql_to_subjects = "INSERT INTO Subjects (SubjectName, TeacherId) VALUES (?, ?)"
    insert_script(conn, sql_to_subjects, subjects)

    sql_to_groups = "INSERT INTO Groups (GroupName) VALUES (?)"
    insert_script(conn, sql_to_groups, groups)

    sql_to_students = "INSERT INTO Students (FirstName, LastName, GroupId) VALUES (?, ?, ?)"
    insert_script(conn, sql_to_students, students)

    sql_to_grades = "INSERT INTO Grades (StudentId, SubjectId, Score, ScoreDate) VALUES (?, ?, ?, ?)"
    insert_script(conn, sql_to_grades, grades)


def select_all(conn, sql_path):
    title_out = [
        "5 студентів із найбільшим середнім балом з усіх предметів",
        "Студент із найвищим середнім балом з певного предмета",
        "Середній бал у групах з певного предмета",
        "Середній бал на потоці (по всій таблиці оцінок)",
        "Курси, які читає певний викладач",
        "Список студентів у певній групі",
        "Оцінки студентів у окремій групі з певного предмета",
        "Середній бал, який ставить певний викладач зі своїх предметів",
        "Список курсів, які відвідує студент",
        "Список курсів, які певному студенту читає певний викладач",
        "Середній бал, який певний викладач ставить певному студентові",
        "Оцінки студентів у певній групі з певного предмета на останньому занятті",
    ]
    try:
        for i in range(1, 13):
            file_name = f"{sql_path}query_{i}.sql"

            if os.path.exists(file_name):
                print(f"{i}. {title_out[i - 1]}:")
                with open(f"{SQL_PATH}query_{i}.sql", "r") as f:
                    sql = f.read()

                result_sql, cur = select_script(conn, sql)

                if result_sql:
                    headers = [description[0] for description in cur.description]
                    print(tabulate(result_sql, headers=headers, tablefmt='fancy_grid'))
                else:
                    print(f"No results for query from {file_name}")
                print("-" * 50)

        return 0
    except Exception as e:
        print(f"Error: An exception occurred - {type(e).__name__}: {e}")
        return -1


if __name__ == '__main__':

    with create_connection(DATABASE) as conn:
        if conn is not None:
            if NEW_TABLES:
                manage_db(conn, 'drop_all_tables.sql')

            manage_db(conn, 'create_all_tables.sql')

            teachers, subjects, groups, students, grades = prepare_data(*generate_fake_data(
                NUMBER_TEACHERS, NUMBER_SUBJECTS, NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_GRADES)
            )

            insert_data_to_bd(conn, teachers, subjects, groups, students, grades)

            select_all(conn, SQL_PATH)

        else:
            print("Error: Cannot create the database connection.")



import csv
import sqlite3

__author__ = 'lli5ba'


def load_course_database(db_name, scv_filename):
    conn = sqlite3.connect(db_name)

    with open(scv_filename, 'rU') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                tupRow = tuple(row)
            with conn:
                cur = conn.curson()
                sql_cmd = "insert into coursedata values(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(sql_cmd, tupRow)


if __name__ == "__main__":
    print ("")
    load_course_database("course1.db", "seas-courses-5years.csv")

    # tuple() turns list into tuple
import csv
import sqlite3

__author__ = 'lli5ba'


def instructor_numbers(dept_id):
    db_name = "course1.db"
    conn = sqlite3.connect(db_name)
    professors = {}
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM coursedata")

        rows = cur.fetchall()

        for row in rows:
            instructor = row[6]
            students = row[4]
            if(row[0] == dept_id):
                if instructor in professors:
                    new_val = professors[instructor] + students
                    professors[instructor] = new_val
                else:
                    professors[instructor] = students
    return professors



if __name__ == "__main__":
    print ("")
    print(instructor_numbers("APMA"))
    # tuple() turns list into tuple
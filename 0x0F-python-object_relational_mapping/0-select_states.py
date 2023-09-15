#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usia
"""


from sys import argv
import MySQLdb


def main():
    """
    main function
    """
    try:
        mysql_user = argv[1]
        mysql_pwd = argv[2]
        db_name = argv[3]

        conn = MySQLdb.connect(
            host="localhost", port=3306, user=mysql_user,
                passwd=mysql_pwd, db=db_name, charset="utf8"
            )
        cur = conn.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
    except Exception as err:
        print(f"Error: {err}")


if __name__ == '__main__':
    main()

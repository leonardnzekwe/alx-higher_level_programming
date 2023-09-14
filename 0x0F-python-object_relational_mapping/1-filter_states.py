#!/usr/bin/python3
"""
a script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""


from sys import argv
import MySQLdb


def main():
    """
    main function
    """
    argc = len(argv) - 1
    if (argc == 3):
        mysql_user = argv[1]
        mysql_pwd = argv[2]
        db_name = argv[3]

        conn = MySQLdb.connect(
                host="localhost", port=3306, user=mysql_user,
                passwd=mysql_pwd, db=db_name, charset="utf8"
            )
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
        )
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()


if __name__ == '__main__':
    main()

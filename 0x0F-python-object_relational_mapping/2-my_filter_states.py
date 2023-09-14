#!/usr/bin/python3
"""
1-filter_states Module
"""


from sys import argv
import MySQLdb


def main():
    """
    main function
    """
    argc = len(argv) - 1
    if (argc == 4):
        mysql_user = argv[1]
        mysql_pwd = argv[2]
        db_name = argv[3]
        state_name = argv[4]

        conn = MySQLdb.connect(
                host="localhost", port=3306, user=mysql_user,
                passwd=mysql_pwd, db=db_name, charset="utf8"
            )
        cur = conn.cursor()
        cur.execute(
                "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC"
                .format(state_name)
            )
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()


if __name__ == '__main__':
    main()

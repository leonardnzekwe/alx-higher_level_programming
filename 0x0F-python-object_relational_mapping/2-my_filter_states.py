#!/usr/bin/python3
"""
a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
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

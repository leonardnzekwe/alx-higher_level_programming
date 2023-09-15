#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
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
        cur.execute(
            """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON states.id = cities.state_id
            ORDER BY cities.id ASC
            """
        )
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
    except Exception as err:
        print(f"Error: {err}")


if __name__ == '__main__':
    main()

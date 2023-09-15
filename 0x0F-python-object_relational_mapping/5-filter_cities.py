#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
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
        state_name = argv[4]

        conn = MySQLdb.connect(
                host="localhost", port=3306, user=mysql_user,
                passwd=mysql_pwd, db=db_name, charset="utf8"
            )
        cur = conn.cursor()
        cur.execute(
            """
            SELECT cities.name
            FROM cities
            JOIN states ON states.id = cities.state_id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """, (state_name,)
        )
        query_rows = cur.fetchall()

        cities_list = []
        for row in query_rows:
            cities_list.append(row[0])
        if cities_list:
            city_names = ', '.join(cities_list)
            print(city_names)
        else:
            print()
        cur.close()
        conn.close()
    except Exception as err:
        print(f"Error: {err}")


if __name__ == '__main__':
    main()

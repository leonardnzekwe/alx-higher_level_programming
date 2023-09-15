#!/usr/bin/python3
"""
a script that lists all City objects from the database hbtn_0e_101_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def main():
    """
    main function
    """
    try:
        user = argv[1]
        pwd = argv[2]
        db = argv[3]

        engine = create_engine(
                f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}',
                pool_pre_ping=True
            )

        Session = sessionmaker(bind=engine)
        session = Session()

        cities = session.query(City).order_by(City.id).all()

        for city in cities:
            print(f"{city.id}: {city.name} -> {city.state.name}")

        session.close()
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()

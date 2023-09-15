#!/usr/bin/python3
"""
a script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
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

        states = session.query(State).order_by(State.id).all()

        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"\t{city.id}: {city.name}")

        session.close()
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()

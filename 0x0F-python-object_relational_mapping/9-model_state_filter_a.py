#!/usr/bin/python3
"""
a script that lists all State objects
that contain the letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


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

        states_with_a = session.query(State).filter(State.name.like('%a%'))
        results = states_with_a.order_by(State.id).all()

        for state in results:
            print(f"{state.id}: {state.name}")

        session.close()
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()

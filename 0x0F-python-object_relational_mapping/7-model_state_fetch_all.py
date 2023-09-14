#!/usr/bin/python3
"""List all State objects from the database hbtn_0e_6_usa."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    main function
    """
    argc = len(argv) - 1
    if (argc == 3):
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


if __name__ == "__main__":
    main()

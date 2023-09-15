#!/usr/bin/python3
"""
a script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
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
        state_name = argv[4]

        engine = create_engine(
                f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}',
                pool_pre_ping=True
            )

        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter(State.name == state_name).first()
        if state:
            print(state.id)
        else:
            print("Not found")

        session.close()
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()

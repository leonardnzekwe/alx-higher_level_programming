#!/usr/bin/python3
"""
a script that changes the name of a
State object from the database hbtn_0e_6_usa
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

        state_to_update = session.query(State).filter_by(id=2).first()

        if state_to_update:
            state_to_update.name = "New Mexico"
            session.commit()
        session.close()
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()

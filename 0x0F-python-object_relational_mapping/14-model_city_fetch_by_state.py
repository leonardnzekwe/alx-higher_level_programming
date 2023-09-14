#!/usr/bin/python3
"""
a script that prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

        query = session.query(State, City).filter(State.id == City.state_id)
        results = query.order_by(City.id).all()

        for state, city in results:
            print(f"{state.name}: ({city.id}) {city.name}")

        session.close()


if __name__ == "__main__":
    main()

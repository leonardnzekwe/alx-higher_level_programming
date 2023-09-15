#!/usr/bin/python3
"""
a script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa
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

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        new_state = State(name="California")
        new_city = City(name="San Francisco")
        new_city.state = new_state

        session.add(new_state)
        session.add(new_city)
        session.commit()
        session.close()
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()

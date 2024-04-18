#!/usr/bin/python3
"""Module retrieves and prints a list of cities with their\
        associated states from a MySQL database using SQLAlchemy.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    # Creates the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Creates a session factory
    Session = sessionmaker(bind=engine)
    # Create a session obj
    session = Session()
    # Retrieves cities and their associated states from the db
    # by joining the City and State tables based on the state_id
    # and ordering the results by city ID
    for city, state in session.query(City, State)\
                              .filter(City.state_id == State.id)\
                              .order_by(City.id):
        # Printing the city and state information
        print("{}: ({}) {}".format(state.name, city.id, city.name))

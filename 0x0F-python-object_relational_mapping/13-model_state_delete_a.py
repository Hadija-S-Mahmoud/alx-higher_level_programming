#!/usr/bin/python3
"""Module that deletes states containing the letter\
        "a" from a MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Creates the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Creates a session factory
    Session = sessionmaker(bind=engine)
    # Creates a session object
    session = Session()
    # Retrieves all states from the database
    for state in session.query(State):
        # Checks if state's name contains the letter "a"
        if "a" in state.name:
            # Del the state from the session
            session.delete(state)
    # Commits the session to persist the changes
    session.commit()

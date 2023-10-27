#!/usr/bin/python3
"""This script lists all state objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}',
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    states = delete(State).where(State.name.contains('a'))
    session.commit()
    session.close()

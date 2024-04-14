#!/usr/bin/python3
"""This module lists out all states that are found in a database table.
The database's name will be passed as a parameter to this script."""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(State).order_by(State.id):
        print("{}: {}".format(row.id, row.name))
    session.close()

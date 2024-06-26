#!/usr/bin/python3
"""This module prints the State class' object whose name property has
the same value as the one that is passed as parameter to this module
from the database hbtn_0e_6_usa"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State) \
                   .filter(State.name == sys.argv[4]) \
                   .first()
    if state:
        print(f"{state.id}")
    else:
        print('Not found')

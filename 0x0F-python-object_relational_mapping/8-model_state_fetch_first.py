#!/usr/bin/python3
"""This script prints out the first record
(object from sqlalchemy perspective) from a
db table via an sqlalchemy api"""

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
    r = session.query(State).first()
    if r:
        print("{}: {}".format(r.id, r.name))
    else:
        print()
        session.close()

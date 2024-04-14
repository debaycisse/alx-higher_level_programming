#!/usr/bin/python3
"""This module takes 3 parameters, which are db credentials, used
to connect to a db and lists out all objects that contains a
letter 'a' in a given table"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    objs = session.query(State) \
                  .filter(State.name.like('%a%')) \
                  .order_by(State.id)
    for obj in objs:
        print("{}: {}".format(obj.id, obj.name))

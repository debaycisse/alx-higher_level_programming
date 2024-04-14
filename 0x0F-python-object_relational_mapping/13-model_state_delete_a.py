#!/usr/bin/python3
"""This module deletes all State objects whose name values contain
the letter a from the database hbtn_0e_6_usa"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    objects_to_be_deleted = session.query(State) \
                                   .filter(State.name.like('%a%')) \
                                   .all()
    for object in objects_to_be_deleted:
        session.delete(object)
    session.commit()
    session.close()

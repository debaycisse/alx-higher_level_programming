#!/usr/bin/python3
"""This module updates an existing object whose id property is equal to
2 in the db table, by changing the value of the key (i.e name) to
'New Mexico' and store the changes to the db table"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    obj = session.query(State).filter(State.id == 2).first()
    obj.name = 'New Mexico'
    session.commit()
    session.close()

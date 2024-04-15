#!/usr/bin/python3
"""This modules prints out State object and their
corresponding City objects, based on their relationship"""

if __name__ == '__main__':
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    state_objs = session.query(State).order_by(State.id).all()
    for state_obj in state_objs:
        print(f'{state_obj.id}: {state_obj.name}')
        for city_obj in state_obj.cities:
            print("\t{}: {}".format(city_obj.id, city_obj.name))
    session.close()

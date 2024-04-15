#!/usr/bin/python3
"""This module lists all City objects from
the database hbtn_0e_101_usa"""

if __name__ == '__main__':
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    city_objs = session.query(City).order_by(City.id).all()
    for city_obj in city_objs:
        print('{}: {} -> {}'.
              format(city_obj.id, city_obj.name, city_obj.state.name))
    session.close()

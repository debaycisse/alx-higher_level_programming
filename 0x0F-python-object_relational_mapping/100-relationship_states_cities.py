#!/usr/bin/python3
"""This module creates a State object with a value
“California” and a City object with a value
“San Francisco” from the database hbtn_0e_100_usa"""

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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cal = State(name='California')
    ct = City(name='San Francisco')
    cal.cities.append(ct)
    session.add_all([cal, ct])
    session.commit()
    session.close()

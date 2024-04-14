#!/usr/bin/python3
"""This module prints all City objects from the database
hbtn_0e_14_usa, along with their joined state or the state
to which they belong"""
if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    for s, c in session.query(State, City) \
                       .filter(State.id == City.state_id) \
                       .order_by(City.id):
        print(f"{s.name}: ({c.id}) {c.name}")
    session.close()

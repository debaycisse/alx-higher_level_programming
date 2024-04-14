#!/usr/bin/python3
"""This module adds the State object “Louisiana” to the database
hbtn_0e_6_usa, using the sqlachemy module's api.
It takes db username, password, and db name and they are used to
establish connection to the database."""

if __name__ == '__main__':
    import sys
    from model_state import State, Base
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    new_obj = State(name='Louisiana')
    session.add(new_obj)
    session.commit()
    print(new_obj.id)
    session.close()

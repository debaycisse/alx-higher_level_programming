#!/usr/bin/python3
"""This module prints out all cities in a database, which is passed as a
parameter to the script. The script joins the cities table with states
table through a foriegn key to the states table"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT c.id, c.name, s.name FROM cities AS c JOIN states\
                AS s ON c.state_id = s.id ORDER BY c.id""")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

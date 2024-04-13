#!/usr/bin/python3
"""This module uses MySQLdb to list out all states
in hbtn_0e_0_usa database"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

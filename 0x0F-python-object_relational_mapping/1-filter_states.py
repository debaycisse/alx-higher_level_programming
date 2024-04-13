#!/usr/bin/python3
"""This module uses MySQLdb to list out states whose name starts
with N (capital letter) from hbtn_0e_0_usa database"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%'")
    for row in cur.fetchall():
        print(row)

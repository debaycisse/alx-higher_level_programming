#!/usr/bin/python3
"""This module fetches and displays a record whose name column's
value matches the parameter, passed to this script"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT id, name FROM states WHERE name = %s ORDER BY id""",
                (sys.argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

#!/usr/bin/python3
"""takes in the name of a state as an argument and
lists all cities of that state, using the database
Args:
    mysql username: name of the user
    mysql password: password for database
    database name: name of the database
    state name: name of state to search
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    INNER JOIN states ON cities.state_id = states.id\
    WHERE states.name = %s\
    ORDER BY cities.id ASC", (argv[4], ))
    c = []
    for row in cur.fetchall():
        c.append(row[1])
    print(", ".join(c))
    cur.close()
    db.close()

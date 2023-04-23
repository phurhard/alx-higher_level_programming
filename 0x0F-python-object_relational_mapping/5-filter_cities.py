#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa

    Your script should take 3 arguments: mysql username, mysql password and database name
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost at port 3306
    Results must be sorted in ascending order by cities.id
    You can use only execute() once
    Results must be displayed as they are in the example below
    Your code should not be executed when imported
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    state = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT  cities.name FROM cities INNER JOIN states ON cities.state_id=states.id WHERE states.name=\"{}\" ORDER BY cities.id ASC".format(state))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

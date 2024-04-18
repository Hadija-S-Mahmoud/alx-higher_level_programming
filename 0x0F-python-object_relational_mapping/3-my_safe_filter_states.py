#!/usr/bin/python3
"""Module that lists all states from the hbtn_0e_0_usa database."""
import sys
import MySQLdb

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Gets the command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connects to the MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Creates a cursor object to execute queries
    cursor = db.cursor()

    # Prepares the SQL query with placeholders
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Executes the query with the state name as a parameter
    cursor.execute(sql_query, (state_name,))

    # Fetches all the rows returned by the query
    rows = cursor.fetchall()

    # Displays the results
    for row in rows:
        print(row)

    # Closes the cursor and database connection
    cursor.close()
    db.close()

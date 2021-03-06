import sqlite3 as lite

con = lite.connect('getting_started.db')

# Inserting rows by passing values directly to `execute()`
# with con:

#    cur = con.cursor()
#    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
#    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
#    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', 85)")
#    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', 95)")

cities = (('Las Vegas', 'NV'),
                    ('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December', 97),
                     ('Atlanta', 2013, 'July', 'January', 87))

# Inserting rows by passing tuples to `execute()`
with con:

    cur = con.cursor()
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
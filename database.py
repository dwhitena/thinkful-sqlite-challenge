import sqlite3 as lite
import pandas as pd
import sys

# cities tuple 
cities_tup = (('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA'))

# weather tuple
weather_tup = (('New York City',   2013,    'July',        'January',     62),
  ('Boston',          2013,    'July',        'January',     59),
  ('Chicago',         2013,    'July',        'January',     59),
  ('Miami',           2013,    'August',      'January',     84),
  ('Dallas',          2013,    'July',        'January',     77),
  ('Seattle',         2013,    'July',        'January',     61),
  ('Portland',        2013,    'July',        'December',    63),
  ('San Francisco',   2013,    'September',   'December',    64),
  ('Los Angeles',     2013,    'September',   'December',    75))

# get user defined month
month = raw_input('Enter a month: ')

# test if month in data
test = month in [t[2] for t in weather_tup]
if test == False:
	print('No cities have an average high in ' + month)
	sys.exit()

# connect to the database
con = lite.connect('getting_started.db')

with con:
	
	cur = con.cursor()
	
	# clear tables if they exist
	cur.execute("DROP TABLE IF EXISTS cities")
	cur.execute("DROP TABLE IF EXISTS weather")
	
	# create cities and weather tables
	cur.execute("CREATE TABLE cities (name text, state text)")
	cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, \
		cold_month text, average_high integer)")
	
	# fill with tuple data
	cur.executemany("INSERT INTO cities VALUES(?,?)", cities_tup)
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather_tup)

	# join data in sqlite
	cur.execute("SELECT name, state, warm_month, average_high FROM weather \
		LEFT OUTER JOIN cities ON city = name \
		WHERE warm_month = " + "'" + month + "'" +\
		" ORDER BY average_high DESC")

	# throw into dataframe
	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows, columns=cols)	

#print("The cities that are warmest in " + month + " are: " + 
print("The cities that are warmest in " + month + " are: " + ", ".join(df["name"].values))
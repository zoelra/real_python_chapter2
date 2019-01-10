import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	make = {'Ford Count': "SELECT count(make) FROM orders WHERE make = 'Ford'",
			'Toyota Count': "SELECT count(make) FROM orders WHERE make = 'Toyota'"}
	model = {'Escape Count': "SELECT count(model) FROM orders WHERE model = 'Escape'",
			'Explorer Count': "SELECT count(model) FROM orders WHERE model = 'Explorer'",
			'F150 Count': "SELECT count(model) FROM orders WHERE model = 'F150'",
			'Civic': "SELECT count(model) FROM orders WHERE model = 'Civic'",
			'Accord': "SELECT count(model) FROM orders WHERE model = 'Accord'"}

	for keys, values in make.items():
		c.execute(values)
		result = c.fetchone()
		print(keys + ":", result[0])

	for keys, values in model.items():
		c.execute(values)
		result = c.fetchone()
		print(keys + ":", result[0])
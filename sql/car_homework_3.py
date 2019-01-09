import sqlite3
import csv

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	orders = csv.reader(open("orders.csv", "rU"))
	
	c.execute("""CREATE TABLE orders(make TEXT, model TEXT, order_date INT)""")

	c.executemany("INSERT INTO orders(make, model, order_date) values (?, ?, ?)", orders)

	c.execute("""SELECT DISTINCT inventory.make, inventory.model, orders.make, orders.model, orders.order_date FROM inventory, orders WHERE inventory.make = orders.make ORDER by inventory.make ASC""")

	rows = c.fetchall()

	for r in rows:
		print("Make: " + r[0] + "," + " Model: " + r[1])
		print("Order Date: " + r[4])
		
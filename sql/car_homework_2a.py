import sqlite3
import csv

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	cars = csv.reader(open("cars.csv", "rU"))

	c.executemany("INSERT INTO inventory(make, model, quantity) values (?, ?, ?)", cars)
	
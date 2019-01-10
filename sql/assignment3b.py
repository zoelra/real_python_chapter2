import sqlite3

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()

	prompt = """Please select which option you'd like to preform:
		1 = Find the minimum value
		2 = Find the maximum value
		3 = Find the average value
		4 = Find the sum of all the values
		5 = Exit the program
My choice is:  """
	print(prompt)
	while True:
		x = input()
		if x in set(["1", "2", "3", "4",]):
			operation = {1:" MIN", 2:" MAX", 3:" AVG", 4:" SUM"}[int(x)]
			c.execute("SELECT{}(num) from numbers".format(operation))
			get = c.fetchone()
			print(operation + ": %f" % get[0])
		elif x == "5":
			print("Thanks!")
			break
		else:
			print("Not a valid entry, please try again with a number 1-5")
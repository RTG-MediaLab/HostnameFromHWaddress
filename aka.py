from csv import DictReader

def alias(addr):
	with open("alias.csv") as f:
		mac = [row["mac"] for row in DictReader(f)]

	with open("alias.csv") as f1:
		aka = [row["aka"] for row in DictReader(f1)]
	print(aka)
 	for i in mac:
		if mac[i] == addr:
      			global fname
      			fname = aka[i]




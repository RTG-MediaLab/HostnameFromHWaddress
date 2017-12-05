from csv import DictReader


with open("alias.csv") as f:
	mac = [row["mac"] for row in DictReader(f)]

with open("alias.csv") as f1:
	aka = [row["aka"] for row in DictReader(f1)]
print(aka)




from csv import DictReader

def alias(addr):
	with open("alias.csv") as f:
		mac = [row["mac"] for row in DictReader(f)]

	with open("alias.csv") as f1:
		aka = [row["aka"] for row in DictReader(f1)]
	print(aka)
 	for i in mac:
		if mac[i] == addr:
      			return aka[i]


if __name__ == "__main__":
    print("this should be ran by another script")

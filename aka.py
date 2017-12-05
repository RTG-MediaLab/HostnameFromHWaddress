from csv import DictReader


f = open("alias.csv", "r")
mac = [row["mac"] for row in DictReader(f)]
alias = [row["aka"] for row in DictReader(f)]

print alias


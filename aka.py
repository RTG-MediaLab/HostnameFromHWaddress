from csv import DictReader


f = open("alias.txt", r)
mac = [row["mac"] for row in DictReader(f)]
alias = [row["aka"] for row in DictReader(f)]

print alias


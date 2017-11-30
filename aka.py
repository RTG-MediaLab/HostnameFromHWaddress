

alias = []
f = open("alias.txt", r)
for line in f:
	line = line.strip()
	alias.append(line)

print alias


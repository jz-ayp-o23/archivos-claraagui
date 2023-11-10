f = open("the Beatles.txt", "r", encoding="utf8")
for line in f:
    print(line.strip())
f.close
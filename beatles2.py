f = open("the Beatles.txt", "r", encoding="utf8")
for line in f:
    for caracter in line:
        print(repr(caracter), end=" ")
    print()
f.close
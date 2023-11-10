with open("the Beatles.txt", "r", encoding="utf8") as f:
    for line in f:
        print(line.strip())
#no es necesario usar close
file=open("Text.txt")
for line in (file.readlines() [-3:]):
    print(line)
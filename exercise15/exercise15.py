file = open("names.txt", "r")
content = file.read()

for line in content.split("\n"):
    print(line)

file.close()

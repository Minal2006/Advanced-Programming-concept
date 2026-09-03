file = open("file1.txt", "r")
lines = file.readlines()
file.close()
for line in reversed(lines):
    print(line.strip())
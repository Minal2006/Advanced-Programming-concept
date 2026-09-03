file = open("file1.txt", "r")
count = 0
for line in file:
    words = line.split()
    count = count + len(words)
file.close()
print("Total number of words:", count)
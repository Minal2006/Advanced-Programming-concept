#Write a program to compare two text files and display whether their contents are identical. If different, identify the first line where they differ.
file1 = open("file1.txt", "w")
file1.write("Python is easy.\n")
file1.write("Python is powerful.\n")
file1.write("Python is popular.\n")
file1.close()

file2 = open("file2.txt", "w")
file2.write("Python is easy.\n")
file2.write("Python is simple.\n")
file2.write("Python is popular.\n")
file2.close()

file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

lines1 = file1.readlines()
lines2 = file2.readlines()

file1.close()
file2.close()

same = True

minimum = min(len(lines1), len(lines2))

for i in range(minimum):
    if lines1[i] != lines2[i]:
        print("Files are different.")
        print("First difference is at line:", i + 1)
        print("File 1:", lines1[i].strip())
        print("File 2:", lines2[i].strip())

        same = False
        break


if same == True:
    if len(lines1) != len(lines2):
        print("Files are different.")
        print("First difference is at line:", minimum + 1)

        if len(lines1) > len(lines2):
            print("File 1 has:", lines1[minimum].strip())
        else:
            print("File 2 has:", lines2[minimum].strip())

        same = False


if same == True:
    print("Both files have identical contents.")












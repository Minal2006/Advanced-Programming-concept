#	Read the contents of two text files and create a third file containing the contents of both files.
file1 = open("file1.txt", "w")
file1.write("This is the first file.\n")
file1.write("It contains some text.\n")
file1.close()
file2 = open("file2.txt", "w")
file2.write("This is the second file.\n")
file2.write("It also contains some text.\n")
file2.close()
file1 = open("file1.txt", "r")
text1 = file1.read()
file1.close()
file2 = open("file2.txt", "r")
text2 = file2.read()
file2.close()
file3 = open("file3.txt", "w")

file3.write(text1)
file3.write(text2)

file3.close()

print("Contents of both files copied into file3.txt successfully.")
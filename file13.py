#Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears.

word = input("Enter the word to search: ")
file = open("file1.txt", "r")
count = 0
line_numbers = []
line_no = 0
for line in file:
    line_no = line_no + 1
    words = line.split()

    for w in words:
        if w.lower() == word.lower():
            count = count + 1
            if line_no not in line_numbers:
                line_numbers.append(line_no)
file.close()
print("Number of occurrences:", count)
if count > 0:
    print("Word found on line numbers:", line_numbers)
else:
    print("Word not found in the file.")
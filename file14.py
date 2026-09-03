#Read a text file and replace all occurrences of a specified word with another word. Save the modified text in the same file or a new file.

file = open("file1.txt", "r")
text = file.read()
file.close()
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
text = text.replace(old_word, new_word)
file = open("student.txt", "w")
file.write(text)
file.close()
print("Word replaced successfully.")
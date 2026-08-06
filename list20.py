books = ["Python", "Java", "C", "C++"]
new_book = input("Enter new book: ")
books.append(new_book)

book = input("Enter book to search: ")
if book in books:
    print("Book found")
else:
    print("Book not found")

remove_book = input("Enter book to remove: ")
books.remove(remove_book)

print("Books:", books)


print("Total Books:", len(books))
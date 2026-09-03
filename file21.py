# 21.	Maintain book records containing book ID, title, author, and availability status. Implement operations to: 
# •	Add a book. 
# •	Search for a book. 
# •	Issue a book. 
# •	Return a book. 
# •	Display available books.

books = []
while True:
    print("\n--- Book Management System ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")

        books.append([book_id, title, author, "Available"])

        print("Book added successfully.")
    elif choice == 2:
        book_id = input("Enter Book ID to search: ")

        found = False

        for book in books:
            if book[0] == book_id:
                print("Book ID:", book[0])
                print("Title:", book[1])
                print("Author:", book[2])
                print("Status:", book[3])
                found = True

        if found == False:
            print("Book not found.")

    elif choice == 3:
        book_id = input("Enter Book ID to issue: ")

        found = False

        for book in books:
            if book[0] == book_id:
                found = True

                if book[3] == "Available":
                    book[3] = "Issued"
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")

        if found == False:
            print("Book not found.")

    elif choice == 4:
        book_id = input("Enter Book ID to return: ")

        found = False

        for book in books:
            if book[0] == book_id:
                found = True

                if book[3] == "Issued":
                    book[3] = "Available"
                    print("Book returned successfully.")
                else:
                    print("Book is already available.")

        if found == False:
            print("Book not found.")
    elif choice == 5:
        print("\nAvailable Books:")

        for book in books:
            if book[3] == "Available":
                print("Book ID:", book[0],
                      "Title:", book[1],
                      "Author:", book[2])

    
    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
def search_book(title):
    books = ["Python Programming", "Java Programming", "Data Structures"]

    if title in books:
        return "Book is available"
    else:
        return "Book is not available"
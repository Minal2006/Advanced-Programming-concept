from books.book_details import book_details
from books.book_search import search_book

from memebers.member_details import member_details
from memebers.member_registration import register_member

from transactions.issue import issue_book
from transactions.return_book import return_book


# Book information
book_id, title, author = book_details()

# Member information
member_id, member_name, phone = member_details()

print("========== LIBRARY APPLICATION ==========")

print("\n----- BOOK INFORMATION -----")
print("Book ID :", book_id)
print("Title   :", title)
print("Author  :", author)

print("\nBook Search:")
print(search_book(title))

print("\n----- MEMBER INFORMATION -----")
print("Member ID :", member_id)
print("Name      :", member_name)
print("Phone     :", phone)

print("\nRegistration:")
print(register_member(member_name))

print("\n----- TRANSACTION INFORMATION -----")
print(issue_book(title, member_name))
print(return_book(title))
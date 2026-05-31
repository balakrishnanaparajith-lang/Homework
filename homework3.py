
books = {
    "Harry Potter": True,
    "Python Basics": True,
    "Data Science Handbook": True
}
borrowers = {}
def display_books():
    print("\nAvailable Books:")
    for book, status in books.items():
        if status:
            print(" -", book)
def issue_book(book_name, borrower):
    if book_name not in books:
        print("Book not found.")
    elif books[book_name] == False:
        print("Book already issued to", borrowers[book_name])
    else:
        books[book_name] = False
        borrowers[book_name] = borrower
        print(borrower, "issued", book_name)
def return_book(book_name, borrower):
    if book_name not in books:
        print("Book not found in library.")
    elif books[book_name] == True:
        print("Book was not issued.")
    else:
        books[book_name] = True
        print(borrower, "returned", book_name)
        borrowers.pop(book_name)
while True:
    print("\n--- Library Menu ---")
    print("1. Issue Book")
    print("2. Return Book")
    print("3. View Available Books")
    print("4. View Borrower List")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        book = input("Enter book name: ")
        borrower = input("Enter borrower name: ")
        issue_book(book, borrower)
    elif choice == "2":
        book = input("Enter book name: ")
        borrower = input("Enter borrower name: ")
        return_book(book, borrower)
    elif choice == "3":
        display_books()
    elif choice == "4":
        print("Borrower Records:", borrowers)
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")



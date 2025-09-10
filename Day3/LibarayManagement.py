class Library:
    def __init__(self):
        self.books = {}   

    def add_book(self, book_id: int, title: str):
        if book_id not in self.books:
            self.books[book_id] = title
            print(f"Book '{title}' added with ID {book_id}")
        else:
            print(f"Book ID {book_id} already exists")

    def remove_book(self, book_id: int):
        if book_id in self.books:
            removed = self.books.pop(book_id)
            print(f"Book '{removed}' with ID {book_id} removed")
        else:
            print("Book ID not found")

    def search_book(self, book_id: int):
        if book_id in self.books:
            print(f"Found → ID: {book_id}, Title: {self.books[book_id]}")
        else:
            print("Book not found")

    def display_books(self):
        if self.books:
            print("Books in Library:")
            for key, value in self.books.items():
                print(f"ID: {key}, Title: {value}")
        else:
            print("Library is empty")

    def total_books(self):
        print(f"Total number of books: {len(self.books)}")

    def clear_books(self):
        self.books.clear()
        print("All books cleared")

    def sort_books(self):
        if self.books:
            sorted_books = dict(sorted(self.books.items(), key=lambda x: x[1].lower()))
            print("Books sorted by Title:")
            for key, value in sorted_books.items():
                print(f"ID: {key}, Title: {value}")
        else:
            print("Library is empty")



def main():
    library = Library()
    cond = True

    while cond:
        print("-----------------------------------------------------------------")
        print(" 1. Add\n 2. Remove\n 3. Search by ID\n 4. Display All\n 5. Total Books\n 6. Clear All\n 7. Sort by Title\n 8. Exit")
        print("-----------------------------------------------------------------")

        try:
            n = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number (1-8).")
            continue

        match n:
            case 1:
                a = int(input("Enter the Book ID: "))
                t = input("Enter the title of the book: ")
                library.add_book(a, t)
            case 2:
                a = int(input("Enter the Book ID to remove: "))
                library.remove_book(a)
            case 3:
                a = int(input("Enter the Book ID to search: "))
                library.search_book(a)
            case 4:
                library.display_books()
            case 5:
                library.total_books()
            case 6:
                library.clear_books()
            case 7:
                library.sort_books()
            case 8:
                cond = False
                print("Thank you for using Library System. Goodbye!")
            case _:
                print("Invalid number. Enter between (1-8)")

if __name__ == "__main__":
    main()

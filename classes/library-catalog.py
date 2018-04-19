'''
Library Catalog
Create a book class with a title, page count, ISBN and whether or not it is checked out or not. Manage a collection of various books and allow the user to check out books or return books. For added complexity generate a report of those books overdue and any fees. Also allow users to put books on reserve.
'''


class Library(object):

    def __init__(self):
        self.book = {}
        self.book_list = []

    def add_book(self, title, author, page_count, ISBN, checked):
        self.book["Title"] = title
        self.book["Author"] = author
        self.book["Page count"] = page_count
        self.book["ISBN"] = ISBN
        self.book["Checked"] = checked
        self.book_list.append(self.book.copy())

    def show_book_list(self):
        print(self.book_list)

    def book_check_out(self, ISBN):
        for book in self.book_list:
            if book["Checked"]:
                if ISBN in book["ISBN"]:
                    book["Checked"] = False
            else:
                print("Book is checked.")

    def book_return(self, ISBN):
        for book in self.book_list:
            if ISBN in book["ISBN"]:
                book["Checked"] = True

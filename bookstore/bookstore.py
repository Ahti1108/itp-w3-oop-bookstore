class Bookstore(object):
    
    def __init__(self, name):
        self.name = name
        self.authors = []
        self.books = []
        
    #gets all the books
    def get_books(self):
        return self.books
    
    #adds book to bookstore
    def add_book(self, book):
        self.books.append(book)
        
        
    def search_books(self, title=None, author=None):
        result = []
        #need help
        for book in self.books:
            if title != None:
                if title.lower() in book.title.lower():
                    result.append(book)
            elif author != None:
                if book.author == author:
                    result.append(book)
        return result

class Author(object):
    
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
    
    #gets all the books
    def get_books(self):
        return self.books

class Book(object):
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.books.append(self)
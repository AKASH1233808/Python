class Library(object):
    books = []
    written_by_author = []
    books_under_price = []

    def __init__(self, name, author, isbn, price):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.price = price

    def addBook(self):
        Library.books.append((self.name,self.author,self.isbn,self.price))
        
    def searchBookISBN(self,isbn):
        for book in Library.books:
            if book[2]==isbn:
                return book

    def searchBookAuthor(self,author):
        for book in Library.books:
            if book[1]==author:
                Library.written_by_author.append(book)
        return Library.written_by_author
        
    
    def searchUnderPrice(self,price):
        for book in Library.books:
            if book[3]<price:
                Library.books_under_price.append(book)
        return Library.books_under_price
        
book = Library('Geometry', 'Jeff Potter', '0596805888', 22)
book.addBook()
book = Library('Math', 'George Harr', '0594805888', 15)
book.addBook()
book = Library('English', 'James Odd', '0596225888', 10)
book.addBook()
book = Library('Physics','Jeff Potter','0597884512',18)
print (book.searchBookISBN('0594805888'))
print (book.searchBookAuthor('George Harr'))
print (book.searchUnderPrice(20))


        



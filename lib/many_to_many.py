class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return all contracts for this author"""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return all books for this author"""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new contract"""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return total royalties from all contracts"""
        return sum(contract.royalties for contract in self.contracts())

    def __repr__(self):
        return f"<Author {self.name}>"
    #pass


class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Return all contracts for this book"""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return all authors for this book"""
        return [contract.author for contract in self.contracts()]

    def __repr__(self):
        return f"<Book {self.title}>"
    #pass


class Contract:
     all = []

def __init__(self, author, book, date, royalties):

        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")

        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")

        if not isinstance(date, str):
            raise Exception("date must be a string")

        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties

        Contract.all.append(self)
@property
def author(self):
        return self._author

@property
def book(self):
        return self._book

@property
def date(self):
        return self._date

@property
def royalties(self):
        return self._royalties

@classmethod
def contracts_by_date(cls, date):
        """Return all contracts for a given date"""
        return [contract for contract in cls.all if contract.date == date]

def __repr__(self):
        return f"<Contract {self.author.name} - {self.book.title}>"
    #pass
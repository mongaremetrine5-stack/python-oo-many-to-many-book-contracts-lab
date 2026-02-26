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
        # Validate inputs
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an int")

        # Assign attributes
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Save to class-level list
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
class Author:
    pass

    def __init__(self, name):
        self.name = name
        self._contracts = []

    def contracts(self):
         return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    pass
    def __init__(self, title):
        self.title = title
        self._bookscontracts = []

    def contracts(self):
        return self._bookscontracts

    def authors(self):
        return [contract.author for contract in self._bookscontracts]


class Contract:
    pass
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception(f'The author is not defined.')
        if not isinstance(book, Book):
            raise Exception(f'The book is not found in the Book class.')
        if not isinstance(date, str):
            raise Exception(f'The date must be a string!')
        if not isinstance(royalties, int):
            raise Exception(f"Royalties are usually of type int so try again.")
        self.author = author
        self.book = book
        self.date = date
        self.royalties =  royalties
        author._contracts.append(self)
        book._bookscontracts.append(self)
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
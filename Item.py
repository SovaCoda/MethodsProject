class Item:
    def __init__(self, isbn, item_number, author, title, publisher, date):
        self.isbn = isbn
        self.item_number = item_number
        self.author = author
        self.title = title
        self.publisher = publisher
        self.date = date

    def edit_info(self, isbn, item_number, author, title, publisher, date):
        self.isbn = isbn
        self.item_number = item_number
        self.author = author
        self.title = title
        self.publisher = publisher
        self.date = date

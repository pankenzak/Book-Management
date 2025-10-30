#Chỗ này để code data của sách
class DataBook:
    def __init__(self, name_book, author, category, producer, quantity):
        self.name_book = name_book
        self.author = author
        self.category = category
        self.producer = producer
        self.quantity = quantity
        
    def print_all_book(self):
        return f'{self.name_book}, {self.author}, {self.category}, {self.producer}, {self.quantity}'
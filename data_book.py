#Chỗ này để code data của sách
class DataBook:
    def __init__(self, id_book:str, name_book:str, author:str, category:str, publication_year:int, producer:str, quantity:int, available:bool, trends:int = 0):
        self.id_book = id_book
        self.name_book = name_book
        self.author = author
        self.category = category
        self.publication_year = publication_year
        self.producer = producer
        self.quantity = quantity
        self.available = available
        self.trends = trends
        
    def det_ID(self):
        return self.id_book

    def author_name(self):
        return self.author
    
    def book_name(self):
        return self.name_book
    

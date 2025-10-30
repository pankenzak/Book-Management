#code giao diện quản lý
from data_book import DataBook
with open('FileBook.txt', 'r') as file: #Doc File sach
    book_list = file.readlines()
    for i in book_list:
        book_materies = i.split('; ') #lay tung quyen sach ra trong list
        import_data = DataBook(book_materies[0], book_materies[1], book_materies[2], book_materies[3], book_materies[4])
        print(import_data.print_all_book()) #Khai bao sach vao va in ra
#code giao diện quản lý
import pandas as pd #truc quan hoa du lieu
from tabulate import tabulate #de ve bang
from data_book import DataBook

def use_data_book():
    
        
        def print_all_book():
            with open('FileBook.txt', 'r') as file_r: #Doc file sach
                book_list = file_r.readlines()
                data_list = [] 
                
                for i in book_list:
                    #lay tung quyen sach ra trong list bang dau hieu '; ' va cat \n o quantity
                    book_materies = [x.strip() for x in i.split('; ')]
                    import_data = DataBook(book_materies[0], book_materies[1], book_materies[2], book_materies[3], book_materies[4], book_materies[5])
                    data_list.append(import_data.__dict__)
                    
                df = pd.DataFrame(data_list)
                df.index = range(1, len(df)+1)
            
            print(tabulate(df, headers = 'keys', tablefmt = 'grid', showindex = True, stralign = 'left'))
                
        def add_book(id_book, name_book, author, category, producer, quantity):
            with open('FileBook.txt', 'a') as file_w: #Mo lai file sach o che do ghi
                file_w.write(f'\n{id_book}; {name_book}; {author}; {category}; {producer}; {quantity}')
            
        def update_book():
            print('dang build update')
            pass
        
        def delete_book():
            print('dang build delete')
            pass
        
        back = False
        while back == False:
            to_do_1 = int(input('\n1. View all book list \n2. Add book\n3. Update book\n4. Delete book\n5. Back\nPleaser enter your choice(1/2/3/4): '))
            if to_do_1 == 1:
                print_all_book()
                
            elif to_do_1 == 2:
                id_book = input('\nEnter id book: ')
                name_book = input('Enter book name: ')
                author = input('Enter author name: ')
                category = input('Enter category: ')
                producer = input('Enter producer: ')
                quantity = int(input('Enter quantity: '))
                add_book(id_book, name_book, author, category, producer, quantity)
                
            elif to_do_1 == 3:
                update_book()
                
            elif to_do_1 == 4:
                delete_book()
                
            elif to_do_1 == 5 :
                back = True
            else:
                continue_or_stop = input('\nWrong input\nIf you want to continue the program please enter "continue" to do\nIf not please enter "stop"\nYour choice: ')
                if continue_or_stop == 'stop':
                  back = True
        
def manager_menu():
  back = False
  while back == False:  #while nay dung de back cua phan lua chon lam gi
    to_do = int(input('\n1. Data books\n2. Search\n3. News\n4. Back \nPleaser enter your choice(1/2/3/4): '))
    if to_do == 1:
        use_data_book()
    if to_do == 4:
        back = True
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
                    import_data = DataBook(book_materies[0], book_materies[1], book_materies[2], book_materies[3], book_materies[4], book_materies[5], book_materies[6], book_materies[7])
                    data_list.append(import_data.__dict__)
                    
                df = pd.DataFrame(data_list)
                df.index = range(1, len(df)+1)
            
            print(tabulate(df, headers = 'keys', tablefmt = 'grid', showindex = True, stralign = 'left'))
                
        def add_book(id_book, name_book, author, category, publication_year, producer, quantity, available):
            with open('FileBook.txt', 'a') as file_w:
                with open('FileBook.txt', 'a+') as file_n:
                    file_n.seek(0, 2)
                    if file_n.tell() > 0:
                        file_n.seek(file_w.tell() - 1)
                        if file_n.read(1) != '\n':    # nếu cuối file chưa có newline thì chèn
                            file_n.write('\n')
                file_w.write(f'{id_book}; {name_book}; {author}; {category}; {publication_year}; {producer}; {quantity}; {available}\n')
            print_all_book()

            
        def update_book():
            with open('FileBook.txt', 'r') as file_u: #Doc file sach
                book_list = file_u.readlines()
                select_book = input('\nEnter the ID book: ')
                for i in book_list:
                    book_materies = [x.strip() for x in i.split('; ')]    
                    select_ID = book_materies[0]
                    if select_book == select_ID:
                        cancel = False
                        update_list = []
                        while cancel == False:
                            what_change = int(input('\n1. Name book\n2. Author\n3. Category\n4. Publication year\n5. Producer\n6. Quantity\n7. Cancel\nEnter your choice(1/2/3/4/5/6/7): '))
                            if what_change == 1:
                                book_materies[1] = input('Enter book name: ')                                
                            elif what_change == 2:
                                book_materies[2] = input('Enter author name: ')
                            elif what_change == 3:
                                book_materies[3] = input('Enter category: ')
                            elif what_change == 4:
                                book_materies[4] = input('Enter producer: ')
                            elif what_change == 5:
                                book_materies[5] = input('Enter producer: ')
                            elif what_change == 6:
                                book_materies[6] = int(input('Enter quantity: '))
                            elif what_change == 7:
                                cancel = True
                                for n in range(0,8):
                                    update_list.append(book_materies[n])
                with open('FileBook.txt', 'w') as file_w:
                    file_w.write('')
                for j in book_list:
                    book_materies = [x.strip() for x in j.split('; ')]
                    select_ID = book_materies[0]
                    with open('FileBook.txt', 'a') as file_w:
                        if select_book != select_ID:
                            file_w.write(f'{book_materies[0]}; {book_materies[1]}; {book_materies[2]}; {book_materies[3]}; {book_materies[4]}; {book_materies[5]}; {book_materies[6]}; {book_materies[7]}\n')
                        elif select_book == select_ID:
                            file_w.write(f'{update_list[0]}; {update_list[1]}; {update_list[2]}; {update_list[3]}; {update_list[4]}; {update_list[5]}; {update_list[6]}; {update_list[7]}\n')
                    
        def delete_book():
            #doc du lieu tu file
            with open('FileBook.txt', 'r') as file_d:
                book_list = file_d.readlines()
            #nhan ID sach can xoa
            delete_id = input('\nEnter the ID book you want to delete: ')
            found = False
            new_list = []
            #tao danh sach moi, bo quyen sach bi xoa
            for line in book_list:
                book_materies = [x.strip() for x in line.split('; ')]
                if book_materies[0] == delete_id:
                    found = True
                    print(f'Book with ID {delete_id} has been deleted')
                    continue
                new_list.append(line.strip())
            #neu khong tim thay ID
            if not found:
                print(f'No book found with ID {delete_id}')
            #ghi lai file sau khi bi xoa
            else:
                with open('FileBook.txt', 'w') as file_w:
                    for line in new_list:
                        file_w.write(line.strip() + '\n')
                print('\n Updated book list after deletion:\n')
                #hien thi lai danh sach sau khi xoa
                data_list = []
                for i in new_list:
                    book_materies = [x.strip() for x in i.split('; ')]
                    import_data = DataBook(book_materies[0], book_materies[1], book_materies[2], book_materies[3], book_materies[4], book_materies[5], book_materies[6], book_materies[7])
                    data_list.append(import_data.__dict__)
                df = pd.DataFrame(data_list)
                df.index = range(1, len(df) + 1)
                print('\nUpdated book list after deletion:\n')
                print(tabulate(df, headers='keys', tablefmt='grid', showindex=True, stralign='left'))
        
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
                publication_year = input('Enter publication_year: ')
                producer = input('Enter producer: ')
                quantity = int(input('Enter quantity: '))
                available = quantity > 0
                add_book(id_book, name_book, author, category, publication_year, producer, quantity, available)
                
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

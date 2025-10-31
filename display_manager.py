#code giao diện quản lý
from data_book import DataBook

def use_data_book():
    with open('FileBook.txt', 'r') as file: #Doc File sach
        book_list = file.readlines()
        
        def print_all_book():
            for i in book_list:
                book_materies = i.split('; ') #lay tung quyen sach ra trong list
                import_data = DataBook(book_materies[0], book_materies[1], book_materies[2], book_materies[3], book_materies[4])
                print(f'\n{import_data.print_all_book()}') #Khai bao sach vao va in ra
                
        def add_book():
            print('dang buil add')
            pass
        
        def update_book():
            print('dang buil update')
            pass
        
        def delete_book():
            print('dang buil delete')
            pass
        
        back = False
        while back == False:
            to_do_1 = int(input('\n1. View all book list \n2. Add book\n3. Update book\n4. Delete book\n5. Back\nPleaser enter your choice(1/2/3/4): '))
            if to_do_1 == 1:
                print_all_book()
            elif to_do_1 == 2:
                add_book()
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
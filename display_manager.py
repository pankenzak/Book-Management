#code giao diện quản lý
from function import print_all_book, add_book, update_book, delete_book, search, top_trending

def use_data_book():
            
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
                select_book = input('\nEnter the ID book: ')
                update_book(False, select_book)
                
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
    to_do = int(input('\n1. Data books\n2. Search\n3. Top trending\n4. Back \nPleaser enter your choice(1/2/3/4): '))
    if to_do == 1:
        use_data_book()
    elif to_do == 2:
        search()
    elif to_do == 3:
        top_trending()
    elif to_do == 4:
        back = True
    


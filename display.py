from function import borrow_display, search, top_trending, use_data_client, login_user, next_day, print_all_book, add_book, update_book, delete_book, read_all_data_files


def user_display(take_MSSV = False):
    
    MSSV = login_user()

    if not take_MSSV:
        back = False
        while not back:
            try:
                print("\n====== USER MENU ======")
                to_do = input("Enter 'N' to next day\n=======================================\n1. Search\n2. Terms\n3. Borrow book\n4. Top trending\n5. Client\n6. Back\nPlease enter your choice (N/1/2/3/4/5): ")
            except ValueError:
                print("Invalid input. Please enter 1, 2, 3, or 4.")
                continue
            
            if to_do.upper() == 'N':
                next_day()
            # ----- OPTION 1: SEARCH -----
            
            elif to_do == '1':
                search()

            # ----- OPTION 2: TERMS -----
            elif to_do == '2':
                print("\n====== LIBRARY TERMS ======")
                try:
                    with open("dieukhoanthuvien.txt", "r", encoding="utf-8") as f:
                        content = f.read()
                        print(content)
                except FileNotFoundError:
                    print("ERROR: Terms file not found.")
                input("\nPress Enter to go back...")

            # ----- OPTION 3: BORROW -----
            elif to_do == '3':
                try:
                    borrow_display(MSSV)
                except FileNotFoundError:
                    print('No news file found.')
                input("\nPress Enter to go back...")
                
            # ----- OPTION 4: TOP TRENDING -----
            elif to_do == '4':
                top_trending()
                
            # ----- Option 5: FIND DATA CLIENT -----
            elif to_do == '5':
                use_data_client()

            # ----- OPTION 6: BACK -----
            elif to_do == '6':
                back = True
            else:
                print("Invalid choice. Please try again.")
                
    else:
        return MSSV

def use_data_book():
            
        back = False
        while back == False:
            to_do_1 = int(input('\n1. View all book list \n2. Add book\n3. Update book\n4. Delete book\n5. Back\nPleaser enter your choice(1/2/3/4): '))
            if to_do_1 == 1:
                print_all_book()
                
            elif to_do_1 == 2:
                with open('FileBook.txt', 'r') as f:
                    book_list = f.readlines()
                id_book = input('\nEnter id book: ')
                name_book = input('Enter book name: ')
                author = input('Enter author name: ')
                category = input('Enter category: ')
                publication_year = input('Enter publication_year: ')
                producer = input('Enter producer: ')
                quantity = int(input('Enter quantity: '))
                available = quantity > 0
                
                check = True
                for i in book_list:
                    book_materies = [x.strip() for x in i.split('; ')]
                    if id_book == book_materies[0]:
                        print('Your ID book has already exist. Please Enter another ID book!')
                        check = False
                        continue
                    elif name_book == book_materies[1]:
                        print('Your book has already exist. Please Enter another book!')
                        check = False
                        continue
                    else:
                        continue   
                if check:
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
    to_do = int(input('\n1. Data books\n2. Data client\n3. Search\n4. Top trending\n5. Back \nPleaser enter your choice(1/2/3/4/5): '))
    if to_do == 1:
        use_data_book()
    elif to_do == 2:
        read_all_data_files()
    elif to_do == 3:
        search(manager = True)
    elif to_do == 4:
        top_trending()
    elif to_do == 5:
        back = True

      

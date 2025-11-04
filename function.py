import pandas as pd #truc quan hoa du lieu
from tabulate import tabulate #de ve bang
from data_book import DataBook

def take_category():
    with open('FileBook.txt', 'r') as f:
        book_list = f.readlines() 
    dict_category = {}
    list_category = []
    for line in book_list:
        book_materies = [x.strip() for x in line.split('; ')]
        list_category.append(book_materies[3])
    set_category = set(list_category)
    for idx, i in enumerate(set_category, 1):
        new_dict = {idx: i}
        dict_category.update(new_dict)
        
    return dict_category

def borrow_display(MSSV, id_book = None):
    
    if id_book == None:
        id_book = input('Enter the ID of the book you want to borrow: ')

    with open('FileBook.txt', 'r') as file_r:
        book_list = file_r.readlines()

    found = False
    updated_list = []
    trend = False
    trend_id = None

    for line in book_list:
        book_materies = [x.strip() for x in line.split('; ')]
        if book_materies[0] == id_book:
            found = True
            quantity = int(book_materies[6])
            if quantity > 0:
                book_materies[6] = str(quantity - 1)
                borrowed_book_name = book_materies[1]
                print(f"\nBạn đã mượn thành công: {borrowed_book_name}")
                trend = True
                trend_id = book_materies[0]     
            else:
                print(f'\nSorry, {book_materies[1]} is not available now')
            updated_list.append('; '.join(book_materies))
        else:
            updated_list.append(line.strip())

    with open('FileBook.txt', 'w', encoding='utf-8') as file_w:
        if updated_list:
            file_w.write('\n'.join(updated_list) + '\n')
            
    if found and quantity > 0:
        # Cập nhật file người dùng
        user_file = f"{MSSV}.txt"
        try:
            # Đọc nội dung hiện tại
            with open(user_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # Cập nhật dòng "Sách đã mượn:"
            for i in range(len(lines)):
                if lines[i].startswith("Sách đã mượn:"):
                    current_books = lines[i].replace("Sách đã mượn:", "").strip()
                    if current_books == "(chưa có)" or current_books == "":
                        lines[i] = f"Sách đã mượn: {borrowed_book_name}\n"
                    else:
                        lines[i] = f"Sách đã mượn: {current_books}, {borrowed_book_name}\n"
                    break

            # Ghi lại file người dùng
            with open(user_file, 'w', encoding='utf-8') as f:
                f.writelines(lines)

            print(f"Đã lưu thông tin mượn vào hồ sơ {user_file}")

        except Exception as e:
            print("Lỗi khi ghi file người dùng:", e)

    if trend and trend_id:
        update_book(True, trend_id)

    if not found:
        print(f'\nBook with ID {id_book} not found')

    print("\nBook list has been updated successfully.")


def display_books(data_list):
    """Hiển thị danh sách sách theo dạng bảng."""
    if not data_list:
        print("\nNo books available.\n")
        return

    df = pd.DataFrame(data_list)
    df.index = range(1, len(df) + 1)
    print(tabulate(df, headers='keys', tablefmt='grid', showindex=True, stralign='left'))


def search():
    
    try:
        with open("FileBook.txt", "r", encoding="utf-8") as f:
            book_list = f.readlines()
    except FileNotFoundError:
        print("ERROR: FileBook.txt not found.")
        

    data_list = []
    for line in book_list:
        book_materies = [x.strip() for x in line.split('; ')]
        if len(book_materies) == 9:
            import_data = DataBook(*book_materies)
            data_list.append(import_data.__dict__)

    back_search = False
    while not back_search:
        try:
            print("\n------ SEARCH FILTER ------")
            choice = int(input("1. All Books\n2. By Book's Name\n3. By Author\n4. By Category\n5. Back\nEnter your choice (1/2/3/4/5): "))
        except ValueError:
            print("Invalid input. Please enter 1, 2, 3, or 4.")
            continue

        # View all books
        if choice == 1:
            display_books(data_list)
            borrow_or_back = input("Enter ID book to borrow a book or enter 'R' to comeback: ")
            if borrow_or_back == 'R':
                continue
            else:
                for i in acc:
                    MSSV = i
                borrow_display(MSSV, borrow_or_back)
                with open("FileBook.txt", "r", encoding="utf-8") as f:
                    book_list = f.readlines()
                data_list = []
                for line in book_list:
                    parts = [x.strip() for x in line.split("; ")]
                    if len(parts) == 9:
                        import_data = DataBook(*parts)
                        data_list.append(import_data.__dict__)

                print("\n=== UPDATED BOOK LIST ===")
                display_books(data_list)
                

        # Search by Book's Name
        elif choice == 2:
            names = sorted(set(book["name_book"] for book in data_list))
            print("\n=== BOOK'S NAME LIST ===")
            for i, name in enumerate(names, 1):
                print(f"{i}. {name}")

            try:
                selected = int(input("\nSelect book number or enter 'R' to comeback: "))
                if selected == 'R':
                    continue
                name = names[selected - 1]
            except (ValueError, IndexError):
                print("Invalid selection.")
                continue

            filtered_books = [b for b in data_list if b["name_book"] == name]
            print(f"\n=== BOOKS BY {name.upper()} ===")
            display_books(filtered_books)
            borrow_or_back = input("Enter ID book to borrow a book or enter 'R' to comeback: ")
            if borrow_or_back == 'R':
                continue
            else:
                for i in acc:
                    MSSV = i
                borrow_display(MSSV, borrow_or_back)
                with open("FileBook.txt", "r", encoding="utf-8") as f:
                    book_list = f.readlines()
                data_list = []
                for line in book_list:
                    parts = [x.strip() for x in line.split("; ")]
                    if len(parts) == 9:
                        import_data = DataBook(*parts)
                        data_list.append(import_data.__dict__)

                print("\n=== UPDATED BOOK LIST ===")
                display_books(data_list)
            
        # Search by Author
        elif choice == 3:
            authors = sorted(set(book["author"] for book in data_list))
            print("\n=== AUTHOR LIST ===")
            for i, author in enumerate(authors, 1):
                print(f"{i}. {author}")

            try:
                selected = int(input("\nSelect author number (0 to go back): "))
                if selected == 0:
                    continue
                author_name = authors[selected - 1]
            except (ValueError, IndexError):
                print("Invalid selection.")
                continue

            filtered_books = [b for b in data_list if b["author"] == author_name]
            print(f"\n=== BOOKS BY {author_name.upper()} ===")
            display_books(filtered_books)
            borrow_or_back = input("Enter ID book to borrow a book or enter 'R' to comeback: ")
            if borrow_or_back == 'R':
                continue
            else:
                for i in acc:
                    MSSV = i
                borrow_display(MSSV, borrow_or_back)
                with open("FileBook.txt", "r", encoding="utf-8") as f:
                    book_list = f.readlines()
                data_list = []
                for line in book_list:
                    parts = [x.strip() for x in line.split("; ")]
                    if len(parts) == 9:
                        import_data = DataBook(*parts)
                        data_list.append(import_data.__dict__)

                print("\n=== UPDATED BOOK LIST ===")
                display_books(data_list)    

        # Search by Category
        elif choice == 4:
            print("\n=== CATEGORIES ===")
            LIST_OF_CATEGORY = take_category()
            for number, name in LIST_OF_CATEGORY.items():
                print(f"{number}. {name}")

            try:
                selected = int(input("Enter category number: "))
                category_name = LIST_OF_CATEGORY.get(selected)
                if not category_name:
                    print("Invalid category number.")
                    continue
            except ValueError:
                print("Please enter a number.")
                continue

            filtered_books = [b for b in data_list if b["category"].lower() == category_name.lower()]
            print(f"\n=== BOOKS IN CATEGORY: {category_name.upper()} ===")
            display_books(filtered_books)
            borrow_or_back = input("Enter ID book to borrow a book or enter 'R' to comeback: ")
            if borrow_or_back == 'R':
                continue
            else:
                for i in acc:
                    MSSV = i
                borrow_display(MSSV, borrow_or_back)
                with open("FileBook.txt", "r", encoding="utf-8") as f:
                    book_list = f.readlines()
                data_list = []
                for line in book_list:
                    parts = [x.strip() for x in line.split("; ")]
                    if len(parts) == 9:
                        import_data = DataBook(*parts)
                        data_list.append(import_data.__dict__)

                print("\n=== UPDATED BOOK LIST ===")
                display_books(data_list)

        elif choice == 5:
            back_search = True
        else:
            print("Invalid choice. Please try again.")
def print_all_book(what_file = 'FileBook.txt'):
    global data_list
    if what_file != 'FileBook.txt':
        with open(what_file, 'r') as file_r: #Doc file sach
            book_list = file_r.readlines()
        data_list = [] 
        
        for i in book_list:
            #lay tung quyen sach ra trong list bang dau hieu '; ' va cat \n o quantity
            book_materies = [x.strip() for x in i.split('; ')]
            import_data = DataBook(book_materies[0], book_materies[1], book_materies[2], book_materies[3], book_materies[4], book_materies[5], book_materies[6], book_materies[7], book_materies[8])
            data_list.append(import_data.__dict__)
    else:
        with open('FileBook.txt', 'r') as file_r:
            book_list = file_r.readlines()
        data_list = []
        for i in book_list:
            #lay tung quyen sach ra trong list bang dau hieu '; ' va cat \n o quantity
            book_materies = [x.strip() for x in i.split('; ')]
            import_data = DataBook(book_materies[0], book_materies[1], book_materies[2], book_materies[3], book_materies[4], book_materies[5], book_materies[6], book_materies[7], book_materies[8])
            data_list.append(import_data.__dict__)
    df = pd.DataFrame(data_list)
    df.index = range(1, len(df)+1)
        
    print(tabulate(df, headers = 'keys', tablefmt = 'grid', showindex = True, stralign = 'left'))

def add_book(id_book, name_book, author, category, publication_year, producer, quantity, available, trends = 0):
            with open('FileBook.txt', 'a') as file_w:
                with open('FileBook.txt', 'a+') as file_n:
                    file_n.seek(0, 2)
                    if file_n.tell() > 0:
                        file_n.seek(file_w.tell() - 1)
                        if file_n.read(1) != '\n':    # nếu cuối file chưa có newline thì chèn
                            file_n.write('\n')
                file_w.write(f'{id_book}; {name_book}; {author}; {category}; {publication_year}; {producer}; {quantity}; {available}; {trends}\n')
            print_all_book()

def update_book(trend = False, select_book = None):
            with open('FileBook.txt', 'r') as file_u: #Doc file sach
                book_list = file_u.readlines()
                update_list = []
                if trend == False:    
                    for i in book_list:
                        book_materies = [x.strip() for x in i.split('; ')]    
                        select_ID = book_materies[0]
                        if select_book == select_ID:
                            cancel = False
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
                                    for n in range(0,9):
                                        update_list.append(book_materies[n])
                else:
                        for i in book_list:
                            book_materies = [x.strip() for x in i.split('; ')]    
                            select_ID = book_materies[0]
                            if select_book == select_ID:
                                trend_point = int(book_materies[8])
                                book_materies[8] = trend_point + 1
                                for n in range(0,9):
                                    update_list.append(book_materies[n])
                with open('FileBook.txt', 'w') as file_w:
                    file_w.write('')
                for j in book_list:
                    book_materies = [x.strip() for x in j.split('; ')]
                    select_ID = book_materies[0]
                    with open('FileBook.txt', 'a') as file_w:
                        if select_book != select_ID:
                            file_w.write(f'{book_materies[0]}; {book_materies[1]}; {book_materies[2]}; {book_materies[3]}; {book_materies[4]}; {book_materies[5]}; {book_materies[6]}; {book_materies[7]}; {book_materies[8]}\n')
                        elif select_book == select_ID:
                            file_w.write(f'{update_list[0]}; {update_list[1]}; {update_list[2]}; {update_list[3]}; {update_list[4]}; {update_list[5]}; {update_list[6]}; {update_list[7]}; {update_list[8]}\n')

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
                print_all_book()            


def top_trending():
    with open('FileBook.txt', 'r') as file_t:
        book_list = file_t.readlines()
    
    compare_list = []
    for line in book_list:
        book_materies = [x.strip() for x in line.split('; ')]
        if len(book_materies) < 9:
            continue
        if not compare_list:
            compare_list.append(book_materies)
            continue
        
        run = True
        for i in compare_list:
            if int(book_materies[8]) >= int(i[8]):
                compare_list.insert(compare_list.index(i), book_materies)
                run = False
                break
        if run:
            compare_list.append(book_materies)

    with open('top_trending.txt', 'w') as file_r:
        file_r.write('')
    with open('top_trending.txt', 'a') as file_t:
        for i in compare_list:
            file_t.write(f'{i[0]}; {i[1]}; {i[2]}; {i[3]}; {i[4]}; {i[5]}; {i[6]}; {i[7]}; {i[8]}\n')
    print_all_book('top_trending.txt')       
            
                      
def use_data_client():    # Nhập id để tìm text xem có của người đó chưa, chưa thì tạo mớimới
    while True:
        print("\n=== Client Data Menu ===")
        MSSV = input('Enter ID customer : ').upper()
        if MSSV == "":
            print('Back menu')
            break

        ID = f"{MSSV}.txt"

        try:
                    # Mở file nếu tồn tại
            with open(ID, 'r', encoding="utf-8") as f:
                data = f.read()
            print("\nCurrent Customer Information:")
            print(data)

        except FileNotFoundError:
            print(f"\nCustomer Information Not Found: {MSSV}")
            client_name = input('Enter Information of New Customer: ').strip()
            with open(ID, 'w', encoding="utf-8") as f:
                f.write(f"ID: {MSSV}\n")
                f.write(f"Tên: {client_name}\n")
                f.write("Borrowed books: (none yet)\n")
                f.write("Number of days remaining to pay: 0\n")
            print(f"\nA new profile has been created for the customer {client_name} (ID: {MSSV})")
            print("The book has been borrowed: (not yet)")
            print("Number of days remaining to pay: 0")

        input("\nPress Enter to return to the user menu...")
        break

            
acc = []            
def login_user():
    print("\n=== USER LOGIN ===")
    MSSV = input("Nhập ID khách hàng (vd: SE203900): ").upper()
    acc.append(MSSV)
    file_name = f"{MSSV}.txt"

    try:
        # Nếu có file → đọc thông tin
        with open(file_name, 'r', encoding='utf-8') as f:
            data = f.read()
        print("\nThông tin khách hàng hiện tại:")
        print(data)
        print("\nĐăng nhập thành công!")
        return MSSV  # trả về ID để dùng cho các thao tác sau
    except FileNotFoundError:
        # Nếu chưa có file → tạo mới
        print("\nChưa có thông tin khách hàng. Tạo hồ sơ mới.")
        name = input("Nhập tên khách hàng: ").strip()
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(f"ID: {MSSV}\n")
            f.write(f"Tên: {name}\n")
            f.write("Sách đã mượn: (chưa có)\n")
            f.write("Số ngày còn lại để trả: 0\n")
        print(f"\nHồ sơ mới đã được tạo cho khách hàng {name} (ID: {MSSV})")
        return MSSV            
            
            


            
            
            
            
            
            
            
            
            
            
            
            
               




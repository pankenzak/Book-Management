#chỗ này để lưu data khách mượn sách và thông tin sách được mượn 

def borrow_display():
    name_user = input('\nEnter your name: ')
    student_id = input('Enter your student ID: ')
    id_book = input('Enter the ID of the book you want to borrow: ')
    with open('FileBook.txt', 'r') as file_r:
        book_list = file_r.readlines()
    found = False
    updated_list = []
    for line in book_list:
        book_materies = [x.strip() for x in line.split('; ')]
        if book_materies[0] == id_book:
            found = True
            quantity = int(book_materies[6])
            if quantity > 0:
                book_materies[6] = str(quantity - 1)
                print(f'\n {name_user} has successfully borrowed {book_materies[1]}')
                with open('BorrowList.txt', 'a') as borrow_file:
                    borrow_file.write(f'{name_user}; {student_id}; {book_materies[0]}; {book_materies[1]}\n')
            else:
                print(f'\nSorry, {book_materies[1]} is not available now')
            updated_list.append('; '.join(book_materies))
        else:
            updated_list.append(line.strip())
        if not found:
            print(f'\nBook with ID {id_book} not found')
        with open('FileBook.txt', 'w') as file_w:
            for line in updated_list:
                file_w.write(line.strip() + '\n')

    print("\nBook list has been updated successfully.")
    
    
    

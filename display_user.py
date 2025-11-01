#Code giao diện user
# def show_menu():
#   print("User menu")
#   print('1. Search')
#   print("2. Term")
#   print('3. News')
#   print('4. Out')
#Dai dong ghi lai thanh mot chuoi cho gon
#Neu dung thi thieu dong input
  
def user_display():
  back = False
  while back == False:
    try:
      to_do = int(input('\n1. Search\n2. Terms\n3. News\n4. Back\nPlease enter your choice(1/2): '))
    except ValueError:
      print("Lựa chọn không phù hợp vui lòng nhập lại 1/2/3/4")
      continue

    if to_do == 1:
      print("FILTER")
      back_1 = False
      while back_1 == False:  #while nay dung de back cua phan Filter
        to_do_1 = int(input('\n1. All\n2. Author\n3. Category\n4. Back\nPlease enter your choice(1/2/3/4): ')) #Nhung input khac doi build data sau do lien ket
        if to_do_1 == 4:  #back ve chon lam gi
          back_1 = True
        elif to_do_1 == 1:
          with open("FileBook.txt", "r", encoding="utf-8") as f:
            ALL_Book = f.read()

        elif to_do_1 == 2:
            try:
                with open("FileBook.txt", "r", encoding="utf-8") as f:
                    lines = f.readlines()
            except :
                print("Không tìm thấy file dữ liệu sách (FileBook.txt).")

        # Bước 1: Tạo danh sách tác giả không trùng
            authors = []
            for line in lines:
                data = [x.strip() for x in line.split(";")]
                if len(data) >= 3:
                    author = data[2]
                    if author not in authors:
                        authors.append(author)

        # Bước 2: Hiển thị danh sách tác giả
            print("\n=== DANH SÁCH TÁC GIẢ ===")
            for i, author in enumerate(authors):
                print(f"{i}. {author}")

        # Bước 3: Người dùng chọn tác giả
            while True:
                try:
                    chon = int(input("\nChọn số tương ứng với tác giả: "))
                    if 0 <= chon <= len(authors):
                        tac_gia_chon = authors[chon]
                        break
                    else:
                        print("Số không hợp lệ, vui lòng nhập lại.")
                except ValueError:
                    print("Vui lòng nhập số hợp lệ.")

        # Bước 4: Hiển thị các sách của tác giả đã chọn
            print(f"\n=== CÁC SÁCH CỦA {tac_gia_chon.upper()} ===")
            found = False
            for line in lines:
                data = [x.strip() for x in line.split(";")]
                if len(data) >= 3 and data[2] == tac_gia_chon:
                    print(f"- {data[1]} (Thể loại: {data[3]}, SL: {data[6]})")
                    found = True
                    
            if not found:
                print("Không tìm thấy sách nào của tác giả này.")
                
        


    elif to_do == 2:
      def hien_thi_dieu_khoan():
        print('LIBRARY TERMS')
        FILE_NAME = "dieukhoanthuvien.txt"
      try:
        with open ('dieukhoanthuvien.txt','r',encoding = 'utf-8') as f:
          NOI_DUNG = f.read()
          print('NOI_DUNG')
      except ValueError:
        print(f"ERROR: NOT TO FOUND THIS FILE '{FILE_NAME}'.")
        print(' TRY ONE MORE AGAIN ') 
      pass
    elif to_do == 3: #chua co flowchart
        import os

# DICTIONARY DÙNG CHO HÀM 'user_display'
LIST_OF_CATEGORY = {
    1: "Fiction",
    2: "Romance",
    3: "Non-Fiction",
    4: "Science Fiction",
    5: "Fantasy",
    6: "Mystery",
    7: "Action & Adventure",
    8: "Horror",
    9: "Historical Fiction",
    10: "Memoir & Autobiography",
    11: "Self-Help",
    12: "Comic & Graphic Novel"
    # (Bạn có thể thêm/sửa thể loại ở đây cho khớp file data của bạn)
}

# --- CODE GIAO DIỆN USER (ĐÃ SỬA) ---
def user_display():
    back = False
    while back == False:
        try:
            # Sửa prompt cho đầy đủ
            to_do = int(input('\n1. Search\n2. Terms\n3. News\n4. Back\nPlease enter your choice(1/2/3/4): '))
        except ValueError:
            print("Lựa chọn không phù hợp vui lòng nhập lại 1/2/3/4")
            continue

        if to_do == 1:
            print("FILTER")
            
            # --- TỐI ƯU HÓA: Đọc file MỘT LẦN ở đây ---
            try:
                with open("FileBook.txt", "r", encoding="utf-8") as f:
                    lines = f.readlines() # lines là một list các dòng
            except FileNotFoundError:
                print("LỖI: Không tìm thấy file dữ liệu sách (FileBook.txt).")
                input("Nhấn Enter để quay lại...")
                continue # Quay lại menu chính

            # Bắt đầu vòng lặp menu con
            back_1 = False
            while back_1 == False:
                try: # Thêm try...except cho menu con
                    to_do_1 = int(input('\n1. All\n2. Author\n3. Category\n4. Back\nPlease enter your choice(1/2/3/4): '))
                except ValueError:
                    print("Lỗi: Vui lòng nhập số 1/2/3/4")
                    continue
                
                if to_do_1 == 4:  # back ve chon lam gi
                    back_1 = True
                    
                elif to_do_1 == 1:
                    print("\n--- TẤT CẢ SÁCH ---")
                    # Sửa: In từng dòng cho dễ đọc
                    if not lines:
                         print("File rỗng.")
                    for line in lines:
                        print(line.strip()) # strip() để xóa xuống dòng thừa
                    print("--------------------")
                    input("Nhấn Enter để tiếp tục...")

                elif to_do_1 == 2:
                    # Bước 1: Tạo danh sách tác giả (đã có 'lines' từ bên ngoài)
                    authors = []
                    for line in lines:
                        # SỬA LỖI LỚN: Dùng split(";")
                        data = [x.strip() for x in line.split(";")] 
                        if len(data) >= 3:
                            author = data[2]
                            if author not in authors:
                                authors.append(author)

                    # Bước 2: Hiển thị danh sách
                    print("\n=== DANH SÁCH TÁC GIA ===")
                    # SỬA LOGIC: Bắt đầu từ 1
                    for i, author in enumerate(authors, 1): 
                        print(f"{i}. {author}")

                    # Bước 3: Người dùng chọn
                    while True:
                        try:
                            chon = int(input("\nChọn số tương ứng với tác giả (Nhập 0 để quay lại): "))
                            if chon == 0:
                                break
                            if 1 <= chon <= len(authors):
                                # SỬA LOGIC: Lấy index [chon - 1]
                                tac_gia_chon = authors[chon - 1] 
                                break
                            else:
                                print("Số không hợp lệ, vui lòng nhập lại.")
                        except ValueError:
                            print("Vui lòng nhập số hợp lệ.")
                    
                    if chon == 0: # Nếu người dùng chọn 0, quay lại menu Filter
                        continue 

                    # Bước 4: Hiển thị sách
                    print(f"\n=== CÁC SÁCH CỦA {tac_gia_chon.upper()} ===")
                    found = False
                    for line in lines:
                        # SỬA LỖI LỚN: Dùng split(";")
                        data = [x.strip() for x in line.split(";")]
                        
                        # SỬA LỖI LỚN: Check len >= 6 và dùng data[5]
                        if len(data) >= 6 and data[2] == tac_gia_chon:
                            print(f"- {data[1]} (Thể loại: {data[3]}, SL/Giá: {data[5]})") 
                            found = True

                    if not found:
                        print("Không tìm thấy sách nào của tác giả này.")
                    input("\nNhấn Enter để tiếp tục...")
                
                # --- CODE TÍCH HỢP TÌM THEO CATEGORY ---
                elif to_do_1 == 3:
                    # Bước 1: Hiển thị menu thể loại
                    print('\n--- Vui lòng chọn thể loại ---')
                    for number, name in LIST_OF_CATEGORY.items():
                        print(f"{number}. {name}")
                    print("---------------------------------")
                    
                    # Bước 2: Người dùng chọn
                    try:
                        chon_so = int(input('Nhập số thể loại bạn muốn tìm: '))
                    except ValueError:
                        print("Lỗi: Vui lòng nhập một con số.")
                        continue # Quay lại menu Filter

                    # Bước 3: Lấy tên thể loại từ số
                    the_loai_chon = LIST_OF_CATEGORY.get(chon_so)
                    if not the_loai_chon:
                        print(f"Lỗi: Số {chon_so} không có trong danh mục.")
                        continue # Quay lại menu Filter

                    # Bước 4: Tìm kiếm và hiển thị sách
                    print(f"\n--- Đang tìm sách thuộc thể loại: '{the_loai_chon}' ---")
                    da_tim_thay = False
                    
                    for line in lines: # Dùng biến 'lines' đã đọc sẵn
                        data = [x.strip() for x in line.split(";")]
                        
                        # So sánh cột thể loại (data[3])
                        if len(data) >= 4 and data[3].lower() == the_loai_chon.lower():
                            print(f"- {data[1]} (Tác giả: {data[2]})")
                            da_tim_thay = True
                            
                    if not da_tim_thay:
                        print("Không tìm thấy cuốn sách nào thuộc thể loại này.")
                    input("\nNhấn Enter để tiếp tục...")


        elif to_do == 2:
            FILE_NAME = "dieukhoanthuvien.txt"
            print('\n--- LIBRARY TERMS ---')
            try:
                with open (FILE_NAME,'r',encoding = 'utf-8') as f:
                    NOI_DUNG = f.read()
                    # SỬA LOGIC: In biến
                    print(NOI_DUNG)
            except FileNotFoundError:
                print(f"ERROR: NOT TO FOUND THIS FILE '{FILE_NAME}'.")
                print(' TRY ONE MORE AGAIN ')
            except Exception as e:
                print(f"Lỗi không xác định: {e}")
            
            input("\nNhấn Enter để quay lại...")
        
       
       

        elif to_do == 4: #Back ve chon man hinh
          back = True
    
 
#chỗ này để code tổng
from display_user import user_display
from display_manager import manager_menu

stop = False
start = True

while start: # hiển thị chon
  choose_display = int(input('1. Manager \n2. User \nPleaser enter your choice(1/2): '))
  
  if choose_display == 1:
    manager_menu()
    
  elif choose_display == 2:
    user_display()
    
  else:  #Output sai
    continue_or_stop = input('\nWrong input\nIf you want to continue the program please enter "continue" to do\nIf not please enter "stop"\nYour choice: ')
    if continue_or_stop == 'stop':
      start = False
  

      

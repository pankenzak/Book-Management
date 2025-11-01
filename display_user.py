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
                    if 1 <= chon <= len(authors):
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
        pass
    elif to_do == 4: #Back ve chon man hinh
      back = True
 

      
        
        
      
      
  


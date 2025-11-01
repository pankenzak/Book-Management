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
      to_do = int(input('\n1. Search\n2. Terms\n3. BestSeller\n4. Back\nPlease enter your choice(1/2): '))
    except ValueError:
      print("Invalid selection please re-enter 1/2/3/4")
      continue

    if to_do == 1:
      print("FILTER")
      back_1 = False
      while back_1 == False:  #while nay dung de back cua phan Filter
        to_do_1 = int(input('\n1. All\n2. Author\n3. Category\n4. Back\nPlease enter your choice(1/2/3/4): ')) #Nhung input khac doi build data sau do lien ket
        if to_do_1 == 4:  #back ve chon lam gi
          back_1 = True
        elif to_do_1 == 1: #All
          with open("FileBook.txt", "r", encoding="utf-8") as f:
            ALL_Book = f.read()
    elif to_do == 2:
      def hien_thi_dieu_khoan():
        print('LIBRARY TERMS')
        FILE_NAME = "dieukhoanthuvien.txt"
      try:
        with open ('dieukhoanthuvien.txt','r',encoding = 'utf-8') as f:
          NOI_DUNG = f.read()
          print('NOI_DUNG')
      except FILE NOT FOUND:
        print(f"ERROR: NOT TO FOUND THIS FILE '{FILE_NAME}'.")
        print(' TRY ONE MORE AGAIN ')
      except 
      pass
    elif to_do == 3: #chua co flowchart
        pass
    elif to_do == 4: #Back ve chon man hinh
      back = True
 
      
        
        
      
      
  

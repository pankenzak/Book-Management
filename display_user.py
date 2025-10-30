#Code giao diện user
def show_menu():
  print("User menu")
  print('1. Search')
  print("2. Term")
  print('3. News')
  print('4. Out')
  
def user_display():
  back = False
  while back == False:  #while nay dung de back cua phan lua chon lam gi
    to_do = int(input('\n1. Search\n2. Terms\n3. News\n4. Back\nPlease enter your choice(1/2): '))
    
    if to_do == 1:
      print("FILTER")
      back_1 = False
      while back_1 == False:  #while nay dung de back cua phan Filter
        to_do_1 = int(input('\n1. All\n2. Author\n3. Category\n4. Back\nPlease enter your choice(1/2/3/4): ')) #Nhung input khac doi build data sau do lien ket
        if to_do_1 == 4:  #back ve chon lam gi
          back_1 = True
    elif to_do == 2: #chua co flowchart
      pass
    elif to_do == 3: #chua co flowchart
        pass
    elif to_do == 4: #Back ve chon man hinh
      back = True
  pass

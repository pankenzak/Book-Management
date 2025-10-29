#chỗ này để code tổng
def manager_display():
  pass

def user_display():
  back = False
  while back = False:  #while nay dung de back cua phan lua chon lam gi
    to_do = int(input('\n1. Search\n2. Terms\n3. News\n4. Back\nPlease enter your choice(1/2): '))
    
    if to_do == 1:
      print("FILTER")
      back_1 = False
      while back_1 = False:  #while nay dung de back cua phan Filter
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

stop = False
start = True

while start:
  choose_display = int(input('1. Manager \n2. User \nPleaser enter your choice(1/2): '))
  
  if choose_display == 1:
    manager_display()
  elif choose_display == 2:
    user_display()
  else:  #Output sai
    continue_or_stop = input('\nWrong input\nIf you want to continue the program please enter "continue" to do\nIf not please enter "stop"\nYour choice: ')
    if continue_or_stop == 'stop':
      start = False

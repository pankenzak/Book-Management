#chỗ này để code tổng
import display_manager.py
import display_user.py

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

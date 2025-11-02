#chỗ này để code tổng
from display_user import user_display
from display_manager import manager_menu
import sys

stop = False
start = True

while start: # hiển thị chon
    choose_display = int(input('1. Manager \n2. User\n3. Shut Down \nPleaser enter your choice(1/2/3): '))
  
    if choose_display == 1:
        manager_menu()
    
    elif choose_display == 2:
        user_display()
    
    elif choose_display == 3:
        sys.exit("See you later!")
     
    else:  #Output sai
        continue_or_stop = input('\nWrong input\nIf you want to continue the program please enter "continue" to do\nIf not please enter "stop"\nYour choice: ')
        if continue_or_stop == 'stop':
            start = False
  
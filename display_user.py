from function import borrow_display, search, top_trending, use_data_client, login_user

def user_display():
    
    MSSV = login_user()
    
    back = False
    while not back:
        try:
            print("\n====== USER MENU ======")
            to_do = int(input("1. Search\n2. Terms\n3. Borrow book\n4. Top trending\n5. Client\n6. Back\nPlease enter your choice (1/2/3/4/5): "))
        except ValueError:
            print("Invalid input. Please enter 1, 2, 3, or 4.")
            continue

        # ----- OPTION 1: SEARCH -----
        if to_do == 1:
            search()

        # ----- OPTION 2: TERMS -----
        elif to_do == 2:
            print("\n====== LIBRARY TERMS ======")
            try:
                with open("dieukhoanthuvien.txt", "r", encoding="utf-8") as f:
                    content = f.read()
                    print(content)
            except FileNotFoundError:
                print("ERROR: Terms file not found.")
            input("\nPress Enter to go back...")

        # ----- OPTION 3: BORROW -----
        elif to_do == 3:
            try:
                borrow_display(MSSV)
            except FileNotFoundError:
                print('No news file found.')
            input("\nPress Enter to go back...")
            
        # ----- OPTION 4: TOP TRENDING -----
        elif to_do == 4:
            top_trending()
            
        # ----- Option 5: FIND DATA CLIENT -----
        elif to_do == 5:
            use_data_client()

        # ----- OPTION 6: BACK -----
        elif to_do == 6:
            back = True
        else:
            print("Invalid choice. Please try again.")


  

      

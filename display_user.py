from function import borrow_display, search


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
}




def user_display():
    back = False
    while not back:
        try:
            print("\n====== USER MENU ======")
            to_do = int(input("1. Search\n2. Terms\n3. Borrow book\n4. Back\nPlease enter your choice (1/2/3/4): "))
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
                borrow_display()
            except FileNotFoundError:
                print('No news file found.')
            input("\nPress Enter to go back...")

        # ----- OPTION 4: BACK -----
        elif to_do == 4:
            back = True
        else:
            print("Invalid choice. Please try again.")


  

      

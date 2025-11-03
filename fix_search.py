# ==========================
# FILE: display_user.py (Updated)
# ==========================

import pandas as pd
from tabulate import tabulate
from data_book import DataBook
from borrow_book import borrow_display

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


def display_books(data_list):
    """Hiển thị danh sách sách theo dạng bảng."""
    if not data_list:
        print("\nNo books available.\n")
        return

    df = pd.DataFrame(data_list)
    df.index = range(1, len(df) + 1)
    print(tabulate(df, headers='keys', tablefmt='grid', showindex=True, stralign='left'))


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
            try:
                with open("FileBook.txt", "r", encoding="utf-8") as f:
                    book_list = f.readlines()
            except FileNotFoundError:
                print("ERROR: FileBook.txt not found.")
                continue

            data_list = []
            for line in book_list:
                book_materies = [x.strip() for x in line.split('; ')]
                if len(book_materies) == 8:
                    import_data = DataBook(*book_materies)
                    data_list.append(import_data.__dict__)

            back_search = False
            while not back_search:
                try:
                    print("\n------ SEARCH FILTER ------")
                    choice = int(input("1. All Books\n2. By Book's Name\n3. By Author\n4. By Category\n5. Back\nEnter your choice (1/2/3/4/5): "))
                except ValueError:
                    print("Invalid input. Please enter 1, 2, 3, or 4.")
                    continue

                # View all books
                if choice == 1:
                    display_books(data_list)
                    input("\nPress Enter to continue...")

                # Search by Book's Name
                elif choice == 2:
                    names = sorted(set(book["name_book"] for book in data_list))
                    print("\n=== BOOK'S NAME LIST ===")
                    for i, name in enumerate(names, 1):
                        print(f"{i}. {name}")

                    try:
                        selected = int(input("\nSelect book number (0 to go back): "))
                        if selected == 0:
                            continue
                        name = names[selected - 1]
                    except (ValueError, IndexError):
                        print("Invalid selection.")
                        continue

                    filtered_books = [b for b in data_list if b["name_book"] == name]
                    print(f"\n=== BOOKS BY {name.upper()} ===")
                    display_books(filtered_books)
                    input("\nPress Enter to continue...")
                    
                # Search by Author
                elif choice == 3:
                    authors = sorted(set(book["author"] for book in data_list))
                    print("\n=== AUTHOR LIST ===")
                    for i, author in enumerate(authors, 1):
                        print(f"{i}. {author}")

                    try:
                        selected = int(input("\nSelect author number (0 to go back): "))
                        if selected == 0:
                            continue
                        author_name = authors[selected - 1]
                    except (ValueError, IndexError):
                        print("Invalid selection.")
                        continue

                    filtered_books = [b for b in data_list if b["author"] == author_name]
                    print(f"\n=== BOOKS BY {author_name.upper()} ===")
                    display_books(filtered_books)
                    input("\nPress Enter to continue...")    

                # Search by Category
                elif choice == 4:
                    print("\n=== CATEGORIES ===")
                    for number, name in LIST_OF_CATEGORY.items():
                        print(f"{number}. {name}")

                    try:
                        selected = int(input("Enter category number: "))
                        category_name = LIST_OF_CATEGORY.get(selected)
                        if not category_name:
                            print("Invalid category number.")
                            continue
                    except ValueError:
                        print("Please enter a number.")
                        continue

                    filtered_books = [b for b in data_list if b["category"].lower() == category_name.lower()]
                    print(f"\n=== BOOKS IN CATEGORY: {category_name.upper()} ===")
                    display_books(filtered_books)
                    input("\nPress Enter to continue...")

                elif choice == 5:
                    back_search = True
                else:
                    print("Invalid choice. Please try again.")

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

        # ----- OPTION 3: BORROW BOOK -----
        elif to_do == 3:
            print("\n====== LIBRARY NEWS ======")
            try:
                borrow_display()
            except FileNotFoundError:
                print("No news file found.")
            input("\nPress Enter to go back...")

        # ----- OPTION 4: BACK -----
        elif to_do == 4:
            back = True
        else:
            print("Invalid choice. Please try again.")


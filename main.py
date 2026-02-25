from __future__ import annotations
from datetime import date
from Library import Library


def print_main_menu() -> None:
    '''method to print main menu 
    args: None
    return: None
    '''
    print('''
            --------------------------------- 
                        Main Menu 
            --------------------------------- 
            1) Add Patron  
            2) Add Book 
            3) Search for Patron 
            4) Search for Book
            5) Check Out Book 
            6) Return Book
                                    99) EXIT 
            --------------------------------- 
            ''')


def print_add_book_menu() -> None:
    '''method to print sub menu 
    args: None
    return: None
    '''
    print('''
            --------------------------------- 
                        Add Book Menu 
            --------------------------------- 
            A) Add Printed Book
            B) Add Ebook
            C) Add Audiobook
            --------------------------------- 
            ''')



def option_1(lib: Library) -> None:
    '''To add a patron'''
    name = input("enter the parton name: ").strip()
    address = input("enter the address: ").strip()
    phone = input("enter the phone number: ").strip()
    # for exception handling 
    if not name:
        print("Patron name cannot be empty.")
        return
    if not address:
        print("Patron address cannot be empty.")
        return
    if not phone:
        print("Patron phone cannot be empty.")
        return
    lib.add_patron(name, address, phone)
    print(f"added patron {name}")


def option_2(lib: Library) -> None:
    '''To add a book'''
    print_add_book_menu()
    choice = input("Choose an option [A|B|C]: ").strip().upper()
    if choice not in {"A", "B", "C"}:
        print("Invalid choice. Try again!!")
        return

    title = input("Enter book title: ")
    if not title:
        print("title can't be empty")
        return

    try:
        if choice == "A":
            num_pages = int(input("Enter number of pages in integers: ").strip())
            lib.add_printed_book(title, num_pages)
        elif choice == "B":
            size_character = int(input("Enter number of characters in the book: ").strip())
            char_per_page = int(input("Enter number of characters that fit in a page:  ").strip())
            lib.add_ebook(title, size_character, char_per_page)
        elif choice == "C":
            dur_seconds = int(input("Enter duration in seconds: ").strip())
            lib.add_audio_book(title, dur_seconds)
        print("Book added!.")

    except ValueError:
        print("Invalid input, try again!.")


def option_3(lib: Library) -> None:
    '''to find a particular patron'''
    name = input("Enter patron's name: ").strip()
    patron = lib.search_patron(name)
    if patron is None:
        print("Parton not found !")
    else:
        print(patron)


def option_4(lib: Library) -> None:
    '''To find a particular book'''
    title = input("Enter book’s title: ").strip()
    book = lib.search_book(title)
    if book is None:
        print("Book not found!")
    else:
        print(book)


def date_converter() -> date | None:
    """ to get date in right format"""

    year = int(input("Enter year (YYYY): ").strip())
    month = int(input("Enter month (MM): ").strip())
    day = int(input("Enter day (DD): ").strip())
    
    return date(month,day,year)


def option_5(lib: Library) -> None:
    '''to check out a book'''
    title = input("Enter book title to check out: ").strip()
    name_p = input("Enter patron name: ").strip()
    
    book = lib.search_book(title)
    if book is None:
        print("Book not found!")
        return

    patron = lib.search_patron(name_p)
    if patron is None:
        print("Patron not found!")
        return

    due = date_converter()

    try:
        lib.check_out_book(book, patron, due) # type: ignore
        print("Book checked out successfully.")
    except Exception as e:  
        print(f"Error while checking out book: {e}")


def option_6(lib: Library) -> None:
    ''' to return a book'''
    title = input("Enter book title to return: ").strip()
    name_p = input("Enter patron name: ").strip()

    book = lib.search_book(title)
    if book is None:
        print("Book not found!")
        return

    patron = lib.search_patron(name_p)
    if patron is None:
        print("Patron not found!")
        return

    try:
        lib.return_book(book, patron)
        print("Book returned")

    except Exception as e:
        print(f"Error while returning book: {e}")


def main() -> None:
    '''Main Program that runs the whole program and calls everything'''
    library_name = input("Enter the name of the library:")
    if not library_name:
        raise RuntimeError("Did not enter the library name")
    lib = Library(library_name)

    while True:
        print_main_menu()
        choice = input("Select a option: ")

        match choice:
            case "1":option_1(lib)
            case "2":option_2(lib)
            case "3":option_3(lib)
            case "4":option_4(lib)
            case "5":option_5(lib)
            case "6":option_6(lib)
            case "99":
                confirm = input("give confirmation that you want to terminate the program (y/n): ").strip().lower()
                if confirm == "y":
                    break
            case _:print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

from __future__ import annotations
from Patron import Patron
from Book import Book
from datetime import date
from Loan import Loan
from LinkedList import LinkedList
from typing import Union,Optional,Tuple
from PrintedBook import PrintedBook
from EBook import EBook
from AudioBook import AudioBook

class Library():
    def __init__(self:Library,name:str) -> None:
        '''Initilaization of Lib object
        args:
            name: the name of lib as str
        returns:
            None'''
        self.__name=name
        self.__patrons=LinkedList()
        self.__books=LinkedList()
        self.__loans=LinkedList()

    @property
    def name(self:Library)->str:
        '''getter for name
        returns: a str that is name'''
        return self.__name

    def add_patron(self:Library,name:str,address:str,phone:str)->None:
        '''searches patron if it does not exist adds it to list
         args:
            name: str that represents a name
            address: str that reprsents address
            phone: a str that reprsents phone number

        returns:
            None
           '''
        if self.search_patron(name) is None:
            P1=Patron(name,address,phone)
            self.__patrons.insert(P1)

      
    def add_printed_book(self:Library,title:str,num_pages:int)->None:
        '''when a book with the given title does not exist already it creates a 
        new PrintedBook and adds it to the printed books list.If the book 
        exists, do nothing.
        args:
            title: name of the book
            num_pages: the number of pages reprsented by int
            
        returns:
                None'''
        if self.search_book(title) is None:
            Pb=PrintedBook(title,num_pages)
            self.__books.insert(Pb)


    def add_ebook(self:Library,title:str,size_chars:int,chars_pp:int)->None:
        ''' when a book with the given title does not exist already it creates a
          new EBook and adds it to the printed books list.If the book exists, do
          nothing.
          args:
                title: name od ebook
                size_chars:int : The number of characters in the book.
                chars_pp:int : The number of characters that fit in a page.
            returns:
                None'''
        if self.search_book(title) is None:
            Eb=EBook(title,size_chars,chars_pp)
            self.__books.insert(Eb)

    def add_audio_book(self:Library,title:str,dur_seconds:int)->None:
        ''' To add a Audio bokk if it already does't exist
        args:
            title: name of the book
            dur_seconds:int : The duration of an audiobook in seconds.
            '''
        if self.search_book(title) is None:
            Ab=AudioBook(title,dur_seconds)
            self.__books.insert(Ab)

     
    def search_book(self:Library,title:str)->Optional[Book|None]:
        '''searches the books list for a book that matches the title. Returns 
        the object or None
        args:
            title: name of the book
        returns:
            a b ook object or none'''
        def _book_title(book:Book)->str:
            '''Helper Function to get name
            returns: a str that gives book title'''
            return book.title
        bt=_book_title
        return self.__books.search(title,bt)
        
    def check_out_book(self:Library,a_book:Book,a_patron:Patron,due:date)->None:
        '''takes a book, a patron and a date’s data (checks object pointers are not null).
           If the book is not checked out, create a Loan object for that book, 
           patron, and date, and add it to the loans list.Adds the book to the 
           patrons (add_checked_book) and the patron to the book (check_out)
           args:
                a_book: name of book
                a_patron: name of patron
                due: the due date
            return:
                None
           '''
        if (a_book is None or a_patron is None or due is None):  # safe pass do nthg
            return
        else:
            if a_book.is_checked_out() is False:
                l1=Loan(a_book,a_patron,due)
                a_book.check_out(a_patron)
                a_patron.add_checked_book(a_book)
                self.__loans.insert(l1)


            
    def return_book(self:Library,a_book:Book,a_patron:Patron)->None:
        '''returns a book back 
        args:
            a-book name of the book
            a_patron: name of the patron'''
        if (a_book is None or a_patron is None ):
            return 
        else:
            def _search_loan(loan:Loan)->Tuple[Book,Patron]:
                '''Helper function to look up loan '''
                return (loan.borrowed_book,loan.checked_out_patron)

            to_find=(a_book,a_patron)
            isloan=self.__loans.search(to_find,_search_loan)

            if isloan is not None:
                a_book.return_book()
                a_patron.remove_checked_book(a_book)
                self.__loans.delete(to_find,_search_loan)



  
    def search_patron(self:Library,name:str)->Optional[Patron|None]:
        '''searches the patrons list for a patron that matches the name. Returns the object or None
        args:
            name: the string that reprsents name of person
        returns:
            the patron or none'''
        def _patron_name(patron:Patron)->str:
            '''Helper Function to get name'''
            return patron.name
        nm=_patron_name
        return self.__patrons.search(name,nm)
        

    def __str__(self:Library) -> str:
        '''Gives string reprsentation of library
        returns:
            a string that reprsents Lib'''
        book_string=[]
        for book in self.__books:
            book_string.append(f"\t\t- {str(book)}")
        final_book="\n".join(book_string)

        patron_string=[]
        for pa in self.__patrons:
            patron_string.append(f"\t\t- {str(pa)}")
        final_patron="\n".join(patron_string)

        loan_string=[]
        for lo in self.__loans:
            loan_string.append(f"\t\t- {str(lo)}")
        final_loan="\n".join(loan_string)

        s=f"Library {self.name}:\n\t- Books:\n {final_book}\n\t- Patrons:\n {final_patron}\n\t- Loans:\n {final_loan}"
        return s

# p1_name="Jane Smith"
# p1_addr="100 Science Dr."
# p1_phone="555-666-5151"
# lib1="Durham Library"
# book1="Harry Potter and the Goblet of Fire"

# lib = Library(lib1)
# lib.add_patron(p1_name,p1_addr,p1_phone)
# lib.add_printed_book(book1, 520)
# due = date(2025, 12, 4)

# p1 = lib.search_patron(p1_name)
# b1 = lib.search_book(book1)
# assert p1 is not None
# assert b1 is not None
# lib.check_out_book(b1, p1, due)
# lib = Library(lib1)

# s = str(lib)
# print(s)
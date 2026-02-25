from __future__ import annotations
from LinkedList import LinkedList

class Patron:
    def __init__(self:Patron,name:str,address:str,phone:str) -> None:
        '''Initializing a Patron.
        args:
            name: name of the patron
            address: address of parton
            phone: phone numbe rof patron
        returns:
            None'''
        self.name=name
        self.address=address
        self.phone_number=phone

        self.__list_checked_books=LinkedList()

    @property
    def name(self:Patron)->str:
        '''getter for name
        return: 
            a str'''
        return self.__name
    @name.setter
    def name(self:Patron,name:str)->None:
        '''setter for name
        args:
            name: str name of patron
        returns:
            None'''
        self.__name=name

    @property
    def address(self:Patron)->str:
        '''getter for address
        returns:
            None'''
        return self.__address
    @address.setter
    def address(self:Patron,address:str)->None:
        '''setter for address
        args:
            address: a str 
        returns:
            None'''
        self.__address=address

    @property
    def phone_number(self:Patron)->str:
        '''getter for phone'''
        return self.__phone_number
    @phone_number.setter
    def phone_number(self:Patron,phone:str)->None:
        '''setter for phone
        args:
            phone: a str 
        returns:
            None'''
        self.__phone_number=phone

    def add_checked_book(self:Patron,book:Book)->None: # type: ignore
        '''adds the book refrence to the checked list
        args:
            book: a book object
        returns:
            None'''
        self.__list_checked_books.insert(book)

    def remove_checked_book(self:Patron,book:Book)->None: # type: ignore
        '''searches for a reference in the checked books list to match 
        the given object. When found, the reference is removed from the 
        list
        args:
            book: a book object
        returns: 
            None'''
        try:
            self.__list_checked_books.delete(book)
        except Exception:
            pass
    def is_book_checked_out_by_patron(self:Patron,book:Book)->bool:# type: ignore
        '''searches for a reference in the checked books list to match 
        the given book object. Returns true when found; false otherwise.
        args: 
            book: a book object
        returns:
            bool'''
        result=self.__list_checked_books.search(book)
        if result !=None:
            return True
        else:
            return False
     
    def __eq__(self:Patron, rhs: Patron) -> bool: # type: ignore
        '''Equality is based on the patron's name.
        args:
            rhs: a patron object
        returns:
            bool'''
        if not isinstance(rhs,Patron):
            return False
        if self.name==rhs.name:
            return True
        else:
            return False
        
    def __str__(self:Patron) -> str:
        '''Gives string reprsentation of Patron
        returns:
            a str'''
        return f"Patron: {self.name}, {self.address} ({self.phone_number}). {len(self.__list_checked_books)} books checked out."
        pass

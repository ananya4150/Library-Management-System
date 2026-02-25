from __future__ import annotations
from Patron import Patron
from typing import Optional
from abc import ABC,abstractmethod

class Book(ABC):

    def __init__(self:Book,title:str) -> None:
        '''Initialize Book attributes
        
            args: 
                title: the name of the book
            returns:
                None
        '''
        self.title=title
        self.__checked_out_by= None
    
    @property
    def title(self:Book)->str:
        '''This is the getter for title
            returns: a string that gives title of book
        '''
        return self.__title
    
    @title.setter
    def title(self:Book,title:str)->None:
        '''This is the setter for title

            args: 
                title: a string reprsenting title of a book
            returns:
                None
        '''
        self.__title=title
    
    def check_out(self:Book,patron:Patron)->None:
        '''This method is used to set the patron who checked out a book 
        
            args:
                patron: a object that reprsents a person
            returns:
                None
        '''
        self.__checked_out_by=patron

    def is_checked_out(self:Book)->bool:
        '''This returns true if the book is already checked out by someone
            returns:
            a bool value that tells if a book is checked out or not
        '''
        if self.__checked_out_by == None:
            return False
        else:
            return True

    def return_book(self:Book)->None:
        '''This is used when a book is returned and sets cehck_out_by to none again'''
        self.__checked_out_by=None

    def get_current_patron(self:Book)->Optional[Patron|None]:
        '''returns the Patron who currently has the book
                returns: the patron who checkd out a book else returns none
        '''
        return self.__checked_out_by
    
    @abstractmethod
    def get_length(self:Book)->str:
        '''this is an abstract method
        returns: a string that reprsents the length
            '''
        raise NotImplementedError

    def __str__(self:Book) -> str:
        '''This is the default string method for Book.'''
        return (f"Book: \"{self.__title}\".")

    def __eq__(self:Book, rhs:object) -> bool:
        '''Check's is two book titles are same.
            args:
                rhs : a object that is a instance of book
            returns:
                a bool value that shows if it is of same type
        '''
        if not isinstance(rhs, Book):
            return False
        if self.title==rhs.title: # type: ignore
            return True
        else:
            return False

    
    
    
    
   

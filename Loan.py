from __future__ import annotations
from Patron import Patron
from Book import Book
from datetime import date

class Loan():
    def __init__(self:Loan,book:Book,patron:Patron,due_date:date|None) -> None:
        """Initializing the loan object
        args:
            book: a book object
            patron: a patron object
            due_date: date 
        returns:
            None
        """
        self.__borrowed_book=book
        self.__checked_out_patron=patron
        self.__due_date=due_date

    @property
    def borrowed_book(self:Loan)->Book:
        '''getter for borrowed book
        returns:
            None'''
        return self.__borrowed_book
    @property
    def due_date(self:Loan)->date|None:
        '''getter for due_date
        Returns: date or none'''
        return self.__due_date
    @property
    def checked_out_patron(self:Loan)->Patron:
        '''getter for checked_out_patron
        returns: a patron object'''
        return self.__checked_out_patron
    
    def __eq__(self:Loan, rhs:Loan) -> bool: # type: ignore
        '''To check equality of book patron and duedate
        args:
            rhs: a object
        returns:
            bool value 
        '''
        if not isinstance(rhs,Loan):
            return False
        if(self.__borrowed_book == rhs.__borrowed_book and self.__due_date == rhs.__due_date and self.__checked_out_patron == rhs.__checked_out_patron):
            return True
        else:
            return False
        
    def __str__(self:Loan) -> str:
        """Basic print string for loan
        returns:  a str rep of loan"""
        if self.__due_date != None:
            return f"Loan of {self.borrowed_book} to {self.checked_out_patron} Due on: {self.due_date.strftime('%m-%d-%Y')}." # type: ignore
        else:
            return f"Loan of {self.__borrowed_book} to {self.__checked_out_patron} Due on: Not Set."
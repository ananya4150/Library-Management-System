from __future__ import annotations
from Book import Book

class PrintedBook(Book):
    def __init__(self:PrintedBook, title: str,num_pages:int) -> None:
        '''Initialize a Printed Book object.
        args:
            title: a str that reprsents title of book
            num_pages:int 
        returns:
            None'''
        super().__init__(title)
        self.__num_pages=num_pages

    @property
    def num_pages(self:PrintedBook)->int:
        '''This is a getter for num of pages.
        returns:
            int'''
        return self.__num_pages

    def get_length(self:PrintedBook) -> str:
        '''Gives length of the book
        returns:
            a str'''
        return f"{self.__num_pages} pages"
    
    def __str__(self:PrintedBook) -> str:
        '''Basic print for printedbook
        returns:
            a str'''
        return super().__str__()+" "+f"Printed {self.get_length()}."
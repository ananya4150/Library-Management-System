from __future__ import annotations
from Book import Book

class EBook(Book):
    def __init__(self:EBook, title: str,size_characters:int,chars_per_page:int) -> None:
        '''Initialize a EBook object.
        args:
            title: str: name of the book
            size_characters: int : The number of characters in the book.
            chars_per_page: int : The number of characters that fit in a page.
        returns:
            None
        '''
        super().__init__(title)
        self.__size_characters=size_characters
        self.__chars_per_page=chars_per_page

    @property
    def size_characters(self:EBook)->int:
        '''This is a getter for size_character.
        returns: 
            int that reprsents size_chr
        '''
        return self.__size_characters
    
    @property
    def chars_per_page(self:EBook)->int:
        '''This is a getter for chars_per_page.
        returns : a int that reprsents chrs per pg
        '''
        return self.__chars_per_page

    def get_length(self:EBook) -> str:
        '''Gives size of the book
        returns: a str rep of length
        
        '''
        return f"size {self.__size_characters}, {self.__chars_per_page} c/p"
    
    def __str__(self:EBook) -> str:
        '''Basic print for Ebook
        returns: a str rep of the book '''
        return super().__str__()+" "+f"Ebook ({self.get_length()})."
    
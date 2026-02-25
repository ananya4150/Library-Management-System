from __future__ import annotations
from Book import Book

class AudioBook(Book):
    def __init__(self:AudioBook, title: str,duration_seconds:int) -> None:
        '''Initialize a Audio Book object.
        args:
            title:(str) The name of the book
            duration_seconds : int : The duration of an audiobook in seconds.
        
        returns:
            None
        '''
        super().__init__(title)
        self.__duration_seconds=duration_seconds

    @property
    def duration_seconds(self:AudioBook)->int:
        '''This is a getter for duration_seconds.
            return : a int that reprsents suration in seconds
        '''
        return self.__duration_seconds

    def get_length(self:AudioBook) -> str:
        '''Gives duration of audio book

            return:   a string reprsentation od duration    
        '''
        return f"{self.__duration_seconds:,} sec"
    
    def __str__(self:AudioBook) -> str:
        '''Basic print for audiobook
            return: a string rep. of audiobook
        '''
        return super().__str__()+" "+f"Audio - Duration: {self.get_length()}."
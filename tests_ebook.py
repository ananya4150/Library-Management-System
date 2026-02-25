from __future__ import annotations
import pytest
from Book import Book
from EBook import EBook

class Patron:
    def __init__(self:Patron, name:str)->None:
        '''Mock Class'''
        self.name = name
title ="Harry Potter and the Goblet of Fire"
pages=520
size=2
chare= 200

def test_case_001()->None:
    '''Testing EBook'''
    eb=EBook(title,size,chare)
    assert eb.size_characters==size ,"size mismatch"
    assert eb.chars_per_page==chare ,"char mismatch"
    assert str(eb) == f'Book: "{title}". Ebook (size {size}, {chare} c/p).' ,"wrong print statement eb"

def test_case_002()->None:
    '''Testing get length'''
    eb=EBook(title,size,chare)
    assert eb.get_length()==f"size {size}, {chare} c/p"

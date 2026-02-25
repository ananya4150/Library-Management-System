from __future__ import annotations
import pytest
from Book import Book
from AudioBook import AudioBook

class Patron:
    def __init__(self:Patron, name:str)->None:
        ''''Mock class'''
        self.name = name
title ="Harry Potter and the Goblet of Fire"
pages=520
duration=32000

def test_case_001()->None:
    '''Testing AudioBook'''
    ab=AudioBook(title,duration)
    assert ab.duration_seconds==duration ,"duration mismatch"
    assert str(ab) == f'Book: "{title}". Audio - Duration: {duration:,} sec.' ,"wrong print statement eb"

def test_case_002()->None:
    '''Testing get length'''
    ab=AudioBook(title,duration)
    assert ab.get_length()==f"{duration:,} sec"

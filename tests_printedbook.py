from __future__ import annotations
import pytest
from Book import Book
from PrintedBook import PrintedBook

class Patron:
    def __init__(self:Patron, name:str)->None:
        '''Mock Class'''
        self.name = name
title ="Harry Potter and the Goblet of Fire"
pages=520

def test_case_001()->None:
    '''Testing PrintedBook'''
    pb=PrintedBook(title,pages)
    assert pb.title==title ,"title mismatch"
    assert pb.num_pages==pages ,"num pages mismatch"
    assert str(pb) == f'Book: "{title}". Printed {pages} pages.' ,"wrong print statement pb"
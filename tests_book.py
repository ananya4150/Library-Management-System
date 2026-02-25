from __future__ import annotations
import pytest

from Book import Book
from PrintedBook import PrintedBook

class Patron:
    def __init__(self:Patron, name:str)->None:
        '''Mock Class'''
        self.name = name

def test_case_001()->None:
    '''Testing Book'''
    pb1=PrintedBook("Harry Potter and the Goblet of Fire",520)
    assert str(pb1) == f"Book: \"Harry Potter and the Goblet of Fire\". Printed 520 pages."
    assert pb1.num_pages==520
    assert pb1.get_length()=="520 pages"

def test_case_002()->None:
    '''Testing Book'''
    patron=Patron("Ananya")
    pb1=PrintedBook("Harry Potter and the Goblet of Fire",520)

    assert pb1.is_checked_out()==False
    assert pb1.get_current_patron()==None

    pb1.check_out(patron)
    assert pb1.is_checked_out()==True
    assert pb1.get_current_patron()==patron

    pb1.return_book()
    assert pb1.is_checked_out()==False

def test_case_003()->None:
    '''Testing Book'''
    pb1=PrintedBook("Harry Potter and the Goblet of Fire",520)
    pb2=PrintedBook("Harry Potter and the Goblet of Fire",520)
    pb3=PrintedBook("Harry",520)
    assert pb1.__eq__(pb2) == True
    assert pb1.__eq__(pb3) == False
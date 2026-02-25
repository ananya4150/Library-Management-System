import pytest
from Patron import Patron
from PrintedBook import PrintedBook
from LinkedList import LinkedList, identity
from Link import Link


def test_case_001_p() -> None:
    '''Testing setters and getters'''
    p1=Patron("Jane Smith", "100 Science Dr","555-666-5151")
    assert p1.name =="Jane Smith" ,"Error in name"
    assert p1.address =="100 Science Dr","error in address"
    assert p1.phone_number == "555-666-5151","error in phone"

    p1.name="Anan"
    p1.address="123 ffkfk"
    p1.phone_number ="122-456-789"
    assert p1.name =="Anan" ,"setter name error"
    assert p1.address =="123 ffkfk" ,"setter address error"
    assert p1.phone_number =="122-456-789" ,"setter phone error"

def test_case_002_p() -> None:
    """ Testing add_checked_book and is_book_checked_out_by_patron """
    
    p1 = Patron("Jane Smith", "100 Science Dr.", "555-666-5151")
    book = PrintedBook("Harry Potter and the Goblet of Fire", 520)
    assert p1.is_book_checked_out_by_patron(book) == False
    p1.add_checked_book(book)
    assert p1.is_book_checked_out_by_patron(book) == True


def test_case_003_p() -> None:
    """remove_checked_book should remove a book that exists in the list."""
    p1 = Patron("Jane Smith", "100 Science Dr.", "555-666-5151")
    book = PrintedBook("Harry Potter and the Goblet of Fire", 520)
    p1.add_checked_book(book)

    assert p1.is_book_checked_out_by_patron(book) == True
    p1.remove_checked_book(book)
    assert p1.is_book_checked_out_by_patron(book) is False


def test_case_004_p() -> None:
    """remove_checked_book should not raise if the book is not in the list."""
    p1 = Patron("Jane Smith", "100 Science Dr.", "555-666-5151")
    book2= PrintedBook("Book", 346)
    p1.remove_checked_book(book2)
    assert p1.is_book_checked_out_by_patron(book2) is False


def test_case_005_p() -> None:
    """testing for multiple books checked out"""
    p1 = Patron("Jane Smith", "100 Science Dr.", "555-666-5151")

    book1 = PrintedBook("Book One", 100)
    book2 = PrintedBook("Book Two", 100)
    p1.add_checked_book(book1)
    assert p1.is_book_checked_out_by_patron(book1) is True
    assert p1.is_book_checked_out_by_patron(book2) is False
    p1.add_checked_book(book2)
    assert p1.is_book_checked_out_by_patron(book1) is True
    assert p1.is_book_checked_out_by_patron(book2) is True


def test_case_006_p() -> None:
    """Testing equality for same name"""
    p1=Patron("Jane Smith", "100 Science Dr","555-666-5151")
    p2=Patron("Jane Smith", "Dr","555-643-5151")
    p3=Patron("Smith", "100 Science Dr","555-666-5151")
    assert p1 == p2  ,"same name not working"
    assert p1 != p3 ,"diffrent name error"


def test_case_007_p() -> None:
    """testing a parton obj against non object"""
    p1=Patron("Jane Smith", "100 Science Dr","555-666-5151")
    assert (p1 == "something") is False   

def test_case_009_p() -> None:
    """testing string outputs"""
    p1 = Patron("Jane Smith", "100 Science Dr.", "555-666-5151")
    s0 = str(p1)
    assert "Patron: Jane Smith, 100 Science Dr." in s0
    assert "0 books checked out." in s0
    book = PrintedBook("Harry Potter and the Goblet of Fire", 520)
    p1.add_checked_book(book)
    s1 = str(p1)
    assert "1 books checked out." in s1
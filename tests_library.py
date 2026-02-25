import pytest
from datetime import date

from Library import Library
from Patron import Patron
from PrintedBook import PrintedBook
from EBook import EBook
from AudioBook import AudioBook

p1_name="Jane Smith"
p1_addr="100 Science Dr."
p1_phone="555-666-5151"
lib1="Durham Library"
book1="Harry Potter and the Goblet of Fire"


def test_case_001_lib() -> None:
    """testing add patron"""
    lib = Library(lib1)
    assert lib.search_patron(p1_name) is None

    lib.add_patron(p1_name,p1_addr,p1_phone)
    assert lib.search_patron("Jane Smith") is not None



def test_case_002_lib() -> None:
    """ Testing adding printed book in the list"""
    
    lib = Library(lib1)
    assert lib.search_book(book1) is None

    lib.add_printed_book(book1, 520)
    assert lib.search_book(book1) is not None


def test_case_003_lib() -> None:
    """ testing adding an ebook and audiobok and searching them in list"""
   
    lib = Library(lib1)
    lib.add_ebook("E-Book", 432, 524)
    lib.add_audio_book("Audio", 23554)

    eb = lib.search_book("E-Book")
    assert isinstance(eb, EBook)

    ab = lib.search_book("Audio")
    assert isinstance(ab, AudioBook)



def test_case_004_lib() -> None:
    """ Testing checking out a book."""
    
    lib = Library(lib1)
    lib.add_patron(p1_name,p1_addr,p1_phone)
    lib.add_printed_book(book1, 520)
    due = date(2025, 12, 4)

    p1 = lib.search_patron(p1_name)
    b1 = lib.search_book(book1)
    assert p1 is not None
    assert b1 is not None

    lib.check_out_book(b1, p1, due)
    assert b1.is_checked_out()
    assert p1.is_book_checked_out_by_patron(b1) is True
    lib.check_out_book(b1, p1, due)
    assert b1.is_checked_out()
    assert p1.is_book_checked_out_by_patron(b1) is True




def test_case_005_lib() -> None:
    """ Testing returning a book"""

    lib = Library(lib1)
    lib.add_patron(p1_name,p1_addr,p1_phone)
    lib.add_printed_book(book1, 520)
    due = date(2025, 12, 4)

    p1 = lib.search_patron(p1_name)
    b1 = lib.search_book(book1)


    assert p1 is not None
    assert b1 is not None

    lib.check_out_book(b1, p1, due)
    lib.return_book(b1,p1)

    assert not b1.is_checked_out()
    assert p1.is_book_checked_out_by_patron(b1) is False


def test_case_006_lib() -> None:
    """testing for returning a book that is not checked out"""
    
    lib = Library(lib1)
    lib.add_patron(p1_name,p1_addr,p1_phone)
    lib.add_printed_book(book1, 520)
    due = date(2025, 12, 4)

    p1 = lib.search_patron(p1_name)
    b1 = lib.search_book(book1)

    assert p1 is not None
    assert b1 is not None
    lib.return_book(b1, p1) 
    assert not b1.is_checked_out()
    assert not p1.is_book_checked_out_by_patron(b1)


def test_case_007_lib() -> None:
    """ Testing string """
    lib = Library(lib1)
    lib.add_patron(p1_name,p1_addr,p1_phone)
    lib.add_printed_book(book1, 520)
    due = date(2025, 12, 4)

    p1 = lib.search_patron(p1_name)
    b1 = lib.search_book(book1)
    assert p1 is not None
    assert b1 is not None
    lib.check_out_book(b1, p1, due)
    

    s = str(lib)
 # text = (
    #     'Library Durham Library:\n'
    #     '\t- Books:\n'
    #     ' \t\t- Book: "Harry Potter and the Goblet of Fire". Printed 520 pages.\n'
    #     '\t- Patrons:\n'
    #     ' \t\t- Patron: Jane Smith, 100 Science Dr. (555-666-5151). 1 books checked out.\n'
    #     '\t- Loans:\n'
    #     ' \t\t- Loan of Book: "Harry Potter and the Goblet of Fire". Printed 520 pages. '
    #     'to Patron: Jane Smith, 100 Science Dr. (555-666-5151). 1 books checked out. '
    #     'Due on: 12-04-2025.'
    # )
    assert "Library Durham Library:" in s
    assert "- Books:" in s
    assert "- Patrons:" in s
    assert "- Loans:" in s
    assert 'Book: "Harry Potter and the Goblet of Fire". Printed 520 pages.' in s
    assert "Patron: Jane Smith, 100 Science Dr. (555-666-5151). 1 books checked out." in s
    assert "Loan of Book: \"Harry Potter and the Goblet of Fire\". Printed 520 pages. to Patron: Jane Smith, 100 Science Dr. (555-666-5151). 1 books checked out. Due on: 12-04-2025." in s
  
   


def test_case_008_lib() -> None:
    """Testing check ouy book without a date obj it does not crash but also checkout does not happen"""
    lib = Library(lib1)
    lib.add_patron(p1_name,p1_addr,p1_phone)
    lib.add_printed_book(book1, 520)
    due = date(2025, 12, 4)

    p1 = lib.search_patron(p1_name)
    b1 = lib.search_book(book1)
    assert p1 is not None
    assert b1 is not None

    lib.check_out_book(b1, p1, None)  # type: ignore

    assert not b1.is_checked_out()
    assert p1.is_book_checked_out_by_patron(b1) is False


def test_case_009_lib() -> None:
    """return_book with None book should not crash and not change state."""
    lib = Library(lib1)
    lib.add_patron(p1_name,p1_addr,p1_phone)
    p1 = lib.search_patron(p1_name)
    assert p1 is not None

    lib.return_book(None, p1)  # type: ignore


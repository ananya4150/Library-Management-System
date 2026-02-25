import pytest
from Patron import Patron
from PrintedBook import PrintedBook
from Book import Book
from datetime import date
from Loan import Loan

p1=Patron("Jane Smith", "100 Science Dr.", "555-666-5151")
b1= PrintedBook("Harry", 520)
due = date(2025, 12, 4)


# def test_case_001_loan() -> None:
#     """Testinf initialization and getters"""
#     loan1 = Loan(b1, p1, due)

#     s=
#     # assert loan1.borrowed_book == b1 ,"Error book"
#     # assert loan1.checked_out_patron ==p1 ,"Error patron"
#     # assert loan1.due_date == due ,"Error date"


def test_case_002_loan() -> None:
    """testing the equality"""
    loan1 = Loan(b1, p1, due)
    loan2 = Loan(b1, p1, due)
    assert loan1 == loan2 ,"Error: same books not equal"
    assert (loan1 == "smth") == False


def test_case_003_loan() -> None:
    """testing equality negative case"""
    b2= PrintedBook("Harry not", 520)

    loan1 = Loan(b1, p1, due)
    loan2 = Loan(b2, p1, due)
    assert loan1 != loan2 ,"Error diffrent book shown same"


def test_case_004_loan() -> None:
    """testing negative equality for diff ppl"""

    p2=Patron("anan", "100 Science Dr.", "555-666-5151")

    loan1 = Loan(b1, p1, due)
    loan2 = Loan(b1, p2, due)
    assert loan1 != loan2 ,"different ppl"


def test_case_005_loan() -> None:
    """different date equality test"""

    loan1 = Loan(b1, p1, due)
    loan2 = Loan(b1, p1, date(2025, 2, 11))
    assert loan1 != loan2 ,"due date error in equality"


def test_case_006_loan() -> None:
    """Testing the string"""
    loan = Loan(b1, p1, due)
    s1 = str(loan)
    s2 = 'Loan of Book: "Harry". Printed 520 pages. to Patron: Jane Smith, 100 Science Dr. (555-666-5151). 0 books checked out. Due on: 12-04-2025.'

    assert s1 == s2


def test_case_007_loan() -> None:
    """testing for not set test"""
    loan = Loan(b1, p1, None) 
    s1 = str(loan)
    assert s1 == 'Loan of Book: "Harry". Printed 520 pages. to Patron: Jane Smith, 100 Science Dr. (555-666-5151). 0 books checked out. Due on: Not Set.'
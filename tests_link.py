import pytest

from Link import Link


def test_case_001_l() -> None:
    """To test get dat,set data and next data"""
    l2 = Link("b")
    l1 = Link("a", l2)
    assert l1.getData() == "a"
    assert l1.getNext() is l2
    assert l2.getNext() is None
    link = Link("c")
    assert link.getData() == "c"
    link.setData('new_data')
    assert link.getData() == 'new_data'
    

def test_case_002_l() -> None:
    """Testing for set next"""
    l1 = Link("a")
    l2 = Link("b")
    l1.setNext(l2)
    assert l1.getNext() is l2
    assert not l1.isLast()
    l1.setNext(None)
    assert l1.getNext() is None
    assert l1.isLast()

def test_case_003_l()->None:
    """testing set next for exception"""
    l1 = Link("a")
    with pytest.raises(Exception, match="Next link must be Link or None"):
        l1.setNext("not a link") # type: ignore

def test_case_004_l() -> None:
    """setNext should raise for anything that is not Link or None."""
    l1 = Link("x")
    with pytest.raises(Exception, match="Next link must be Link or None"):
        l1.setNext("not a link")  # type: ignore[arg-type]


def test_case_005_l() -> None:
    """isLast returns True only when next is None."""
    l2 = Link(3)
    l1 = Link(2, l2)
    assert l2.isLast() is True
    assert l1.isLast() is False


def test_case_006_l() -> None:
    """testing strings print"""
    link_int = Link(1)
    link_str = Link("Ananya")
    assert str(link_int) == "1"
    assert str(link_str) == "Ananya"

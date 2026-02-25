import pytest
from LinkedList import LinkedList, identity
from Link import Link


def test_case_001_ll() -> None:
    '''testing for an empty linkedlist, str,and length'''
    l1 = LinkedList()
    assert l1.isEmpty() is True
    assert len(l1) == 0 ,"length issue"
    assert str(l1) == "[]"

def test_case_002_ll()->None:
    '''Testing for getters and setters'''
    l1 = LinkedList()
    assert l1.getFirst() is None
    assert l1.getNext() is None
    link1=Link("a")
    l1.setFirst(link1)
    assert l1.getFirst() is link1
    assert l1.getNext() is link1

def test_case_003_ll()->None:
    '''testing setter for invalid casee'''
    l1 = LinkedList()
    with pytest.raises(Exception, match="First link must be Link or None"):
        l1.setFirst("blabla")    # type: ignore
    with pytest.raises(Exception, match="First link must be Link or None"):
        l1.setNext(123) # type: ignore


def test_case_004_ll() -> None:
    '''testing if insert adds at start of list'''
    l1 = LinkedList()
    l1.insert(3)
    l1.insert(2)
    l1.insert(1)   
    assert l1.isEmpty() is False , "list is not empty initially"
    assert len(l1) == 3 ,"length issue"
    assert l1.first() == 1
    assert str(l1) == "[1 > 2 > 3]"


def test_case_005_ll() -> None:
    '''testing exception for first '''
    l1 = LinkedList()
    with pytest.raises(Exception, match="No first item in empty list"):
        l1.first()


def test_case_006_ll() -> None:
    '''Testing trasvers to apply fucntions'''
    l1 = LinkedList()
    l1.insert(1)
    l1.insert(2)
    l1.insert(3)
    seen= []
    def collect(x: int) -> None:
        '''helper function to append a list'''
        seen.append(x)

    l1.traverse(collect)
    assert seen == [3, 2, 1]


def test_case_007_ll() -> None:
    ''''Testing find and search by identity'''
    l1 = LinkedList()
    l1.insert(1)
    l1.insert(2)
    l1.insert(3)
    link = l1.find(2)              
    assert link is not None
    assert link.getData() == 2
    assert l1.search(3) == 3
    assert l1.search(4) is None      


# def test_case_008_ll() -> None:
#     '''testing find and search for specific key'''
#     l1 = LinkedList()
#     l1.insert({"id": 1, "name": "a"})
#     l1.insert({"id": 2, "name": "b"}) 

#     key = lambda d: d["id"]
#     link = lst.find(1, key=key)
#     assert link is not None
#     assert link.getData()["name"] == "a"

#     result = lst.search(2, key=key)
#     assert result["name"] == "b"


def test_case_008_ll() -> None:
    '''testing insert and print statement'''
    l1 = LinkedList()
    l1.insert(1)
    l1.insert(2)
    l1.insert(3)

    t1 = l1.insertAfter(2, 33)
    assert t1 is True
    assert str(l1) == "[3 > 2 > 33 > 1]"
    t2 = l1.insertAfter(44, 5)
    assert t2 is False
    assert str(l1) == "[3 > 2 > 33 > 1]"


def test_case_009_ll() -> None:
    '''testing single and multiple delete'''
    l1 = LinkedList()
    l1.insert("1")
    l1.insert("2")   
    removed = l1.deleteFirst()
    assert removed == "2"
    assert str(l1) == "[1]"
    assert l1.first() == "1"
    removed2 = l1.deleteFirst()
    assert removed2 == "1"
    assert l1.isEmpty() is True
    assert str(l1) == "[]"


def test_case_010_ll() -> None:
    '''testing delete first exception'''
    l1 = LinkedList()
    with pytest.raises(Exception, match="Cannot delete first of empty list"):
        l1.deleteFirst()


def test_case_011_ll() -> None:
    '''testing delete for head,middle,and not found'''
    l1 = LinkedList()
    l1.insert(1)
    l1.insert(2)
    l1.insert(3)
    removed_mid = l1.delete(2)
    assert removed_mid == 2
    assert str(l1) == "[3 > 1]"
    removed_head = l1.delete(3)
    assert removed_head == 3
    assert str(l1) == "[1]"
    with pytest.raises(Exception, match="No item with matching key"):
        l1.delete(2)


def test_case_012_ll() -> None:
    '''testing empty exception for delete'''
    l1 = LinkedList()
    with pytest.raises(Exception, match="Cannot delete from empty linked list"):
        l1.delete(1)

def test_case_013_ll()->None:
    '''Testing the iterator'''
    l1 = LinkedList()
    l1.insert("A")
    loop = iter(l1)
    assert next(loop) == "A"
    with pytest.raises(StopIteration):
        next(loop)


def test_case_015_ll() -> None:
    """Testing that LinkedList ite"""
    l1 = LinkedList()
    l1.insert("1")
    l1.insert("2")
    l1.insert("3") 

    data = [x for x in l1]
    assert data == ["3", "2", "1"]

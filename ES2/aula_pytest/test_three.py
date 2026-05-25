import pytest
from cards import Card


def test_field_access():
    c = Card("something", "Jhon", "todo", 123)
    assert c.summary == "something"
    assert c.owner == "Jhon"
    assert c.state == "todo"
    assert c.id == 123


def test_defaults():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None


def test_equality():
    c1 = Card("something", "Jhon", "todo", 123)
    c2 = Card("something", "Jhon", "todo", 123)
    assert c1 == c2


def test_equality_with_diff():
    c1 = Card("something", "Jhon", "todo", 123)
    c2 = Card("something", "Jhon", "todo", 4567)
    assert c1 == c2


def test_inequality():
    c1 = Card("something", "Jhon", "todo", 123)
    c2 = Card("completely different", "Paul", "done", 123)
    assert c1 != c2


def test_from_dict():
    c1 = Card("something", "Jhon", "todo", 123)
    c2_dict = {"summary": "something", "owner": "Jhon", "state": "todo", "id": 123}
    c2 = Card.from_dict(c2_dict)
    assert c1 == c2


def test_to_dict():
    c1 = Card("something", "Jhon", "todo", 123)
    c2 = c1.to_dict()
    c2_expected = {"summary": "something", "owner": "Jhon", "state": "todo", "id": 123}
    assert c2 == c2_expected


def test_with_fail():
    c1 = Card("sit there", "Jhon")
    c2 = Card("do something", "Paul")

    if c1 != c2:
        pytest.fail("they don't match")


def test_no_path_raises():
    with pytest.raises(TypeError):
        cards.CardDB()

# from pathlib import Path
# from tempfile import TemporaryDirectory

# import cards


# def test_empty():
#     with TemporaryDirectory() as db_dir:
#         db_path = Path(db_dir)
#         db = cards.CardsDB(db_path)

#         count = db.count()
#         db.close()

#         assert count == 0

# import time
# from pathlib import Path
# from tempfile import TemporaryDirectory

# import cards
# import pytest


# @pytest.fixture
# def cards_db():
#     with TemporaryDirectory() as db_dir:
#         db_path = Path(db_dir)
#         db = cards.CardsDB(db_path)
#         yield db
#         db.close()


# def test_empty(cards_db):
#     assert cards_db.count() == 0


# def test_two(cards_db):
#     cards_db.add_card(cards.Card("First"))
#     cards_db.add_card(cards.Card("Second"))

#     assert cards_db.count() == 2

# =======================================================
# import time
# from pathlib import Path
# from tempfile import TemporaryDirectory

# import cards
# import pytest


# @pytest.fixture(scope="module")
# def cards_db():
#     with TemporaryDirectory() as db_dir:
#         db_path = Path(db_dir)
#         db = cards.CardsDB(db_path)
#         # time.sleep(1)
#         yield db
#         db.close()


# def test_empty(cards_db):
#     assert cards_db.count() == 0


# def test_two(cards_db):
#     cards_db.add_card(cards.Card("First"))
#     cards_db.add_card(cards.Card("Second"))

#     assert cards_db.count() == 2


# def test_three(cards_db):
#     # consigo mudar para function novamente
#     cards_db.add_card(cards.Card("First"))
#     cards_db.add_card(cards.Card("Second"))
#     cards_db.add_card(cards.Card("Third"))
#     assert cards_db.count() == 3

# =========================== solucionar usando duas fixtures ========================

import time
from pathlib import Path
from tempfile import TemporaryDirectory

import cards
import pytest

# @pytest.fixture(scope="session")
# def db():
#     with TemporaryDirectory() as db_dir:
#         db_path = Path(db_dir)
#         db = cards.CardsDB(db_path)
#         # time.sleep(1)
#         yield db
#         db.close()


# @pytest.fixture(scope="function")
# def cards_db(db):
#     db.delete_all()
#     return db


def test_empty(cards_db):
    assert cards_db.count() == 0


def test_two(cards_db):
    cards_db.add_card(cards.Card("First"))
    cards_db.add_card(cards.Card("Second"))

    assert cards_db.count() == 2


def test_three(cards_db):
    # consigo mudar para function novamente
    cards_db.add_card(cards.Card("First"))
    cards_db.add_card(cards.Card("Second"))
    cards_db.add_card(cards.Card("Third"))
    assert cards_db.count() == 3


def test_add_some(cards_db, some_cards):
    expected_count = len(some_cards)

    for c in some_cards:
        cards_db.add_card(c)
    assert cards_db.count() == expected_count


def test_non_empty(non_empty_db):
    assert non_empty_db.count() > 0

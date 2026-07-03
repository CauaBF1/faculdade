import time
from pathlib import Path
from tempfile import TemporaryDirectory

import cards
import pytest


@pytest.fixture(scope="session")
def db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        # time.sleep(1)
        yield db
        db.close()


@pytest.fixture(scope="function")
def cards_db(db):
    db.delete_all()
    return db


@pytest.fixture(scope="session")
def some_cards():
    return [
        cards.Card("Write book", "Brian", "done"),
        cards.Card("edit book", "Katie", "done"),
        cards.Card("Write second book", "Brian", "todo"),
        cards.Card("edit second book", "Katie", "todo"),
    ]


@pytest.fixture(scope="function")
def non_empty_db(cards_db, some_cards):
    for c in some_cards:
        cards_db.add_card(c)
    return cards_db

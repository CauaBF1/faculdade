from pathlib import Path
from tempfile import TemporaryDirectory

import cards
import pytest


@pytest.fixture(scope="module")
# com module só executou uma vez
def retorna_string():
    print()
    yield "Caua"
    print()


@pytest.fixture(scope="session")
def retorna_lista():
    return ["caua", 20, "araxa", "masculino"]


@pytest.fixture(scope="module")
def retorna_dicionario():
    return {"Caua": 19, "Lucas": 20}


def test_retorna_string(retorna_string):
    assert "Caua" == retorna_string


def test_retorna_string2(retorna_string):
    assert "caua" != retorna_string

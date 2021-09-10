#!/usr/bin/env python
import pytest
import database

# Starting with a fixture that automatically runs before each test
@pytest.fixture
def db_mock():
    return database.Database("src/data/db.json")


def test_balance(db_mock):
    """
    Test the balance() method. This does NOT follow TDD as it is written for an exisiting code
    :param db_mock:
    :return:
    """
    assert db_mock.balance("ACCT100") == "40.00 USD"
    assert db_mock.balance("ACCT200") == "-10.00 USD"
    assert db_mock.balance("ACCT300") == "0.00 USD"
    assert db_mock.balance("7ammo") is None


def test_owes_money(db_mock):
    """
    Follows TDD
    :param db_mock:
    :return: .
    """
    assert db_mock.owes_money("ACCT100")
    assert not db_mock.owes_money("ACCT200")
    assert not db_mock.owes_money("ACCT300")
    assert db_mock.owes_money("7amo") is None


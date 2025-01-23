import pytest
import datetime
from . import bitcoin_wallet


TEST_WALLET_ID = "3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC"


def test_get_total_sent_returns_float():
    """
    Test that the get_total_sent function returns a float.
    """
    # Create a wallet and get total sent
    wallet = bitcoin_wallet.Wallet(TEST_WALLET_ID)
    total_sent = wallet.get_total_sent()

    assert type(total_sent) == float


def test_get_total_received_returns_float():
    """
    Test that the get_total_received function returns a float.
    """
    # Create a wallet and get total sent
    wallet = bitcoin_wallet.Wallet(TEST_WALLET_ID)
    total_received = wallet.get_total_received()

    assert type(total_received) == float


def test_get_current_balance_returns_float():
    """
    Test that the get_current_balance function returns a float.
    """
    # Create a wallet and get total sent
    wallet = bitcoin_wallet.Wallet(TEST_WALLET_ID)
    current_balance = wallet.get_current_balance()

    assert type(current_balance) == float


def test_get_first_seen_returns_datetime():
    """
    Test that the get_first_seen function returns a datetime.
    """
    # Create a wallet and get total sent
    wallet = bitcoin_wallet.Wallet(TEST_WALLET_ID)
    first_seen = wallet.get_first_seen()

    assert type(first_seen) == datetime.datetime


def test_wallet_exists_true():
    """
    Tests that a known wallet exists.
    """
    wallet = bitcoin_wallet.Wallet(TEST_WALLET_ID)
    exists = wallet.get_exists()

    assert exists == True


def test_wallet_exists_false():
    """
    Tests that a made up wallet does not exists.
    """
    wallet = bitcoin_wallet.Wallet("MADE-UP-WALLET")
    exists = wallet.get_exists()

    assert exists == False


def test_get_transaction_count_returns_int():
    """
    Tests that the correct number of transactions is returned.
    """
    wallet = bitcoin_wallet.Wallet(TEST_WALLET_ID)
    transaction_count = wallet.get_transaction_count()

    assert type(transaction_count) == int


def test_get_current_balance_fiat_returns_float():
    """
    Tests that a currency is returned in float form.
    """
    wallet = bitcoin_wallet.Wallet(TEST_WALLET_ID)
    transaction_count = wallet.get_current_balance_fiat("GBP")

    assert type(transaction_count) == float

import requests
import json
from datetime import datetime
from statistics import mean
from datetime import datetime


class Wallet:
    def __init__(self, address):
        self.address = address

    def get_exists(self) -> bool:
        """
        Returns True if the wallet exsist.

        Parameters:
        wallet_id (str): The bitcoin wallet to check.

        Returns:
        (bool): Does the wallet exist
        """
        response = requests.get(
            f"https://blockchain.info/q/addressfirstseen/{self.address}")
        try:
            datetime.fromtimestamp(response.json())
            return True
        except:
            return False

    def get_total_sent(self) -> float:
        """
        Returns the total amount of bitcoin sent by a wallet.

        Parameters:
        wallet_id (str): The bitcoin wallet to get total sent from.

        Returns:
        (float): Amount of bitcoin sent from a wallet.
        """
        response = requests.get(
            f"https://blockchain.info/q/getsentbyaddress/{self.address}")
        # Convert from sats to btc divide by 100,000,000
        return int(response.json()) / 100000000

    def get_total_received(self) -> float:
        """
        Returns the total amount of bitcoin received by a wallet.

        Parameters:
        wallet_id (str): The bitcoin wallet to get total received from.

        Returns:
        (float): Amount of bitcoin received by a wallet.
        """
        response = requests.get(
            f"https://blockchain.info/q/getreceivedbyaddress/{self.address}")
        # Convert from sats to btc divide by 100,000,000
        return int(response.json()) / 100000000

    def get_current_balance(self) -> float:
        """
        Returns the amount of bitcoin currently in a given wallet.

        Parameters:
        btc_address (str): The bitcoin wallet to get amount from.

        Returns:
        (float): Amount of bitcoin in given wallet.
        """
        response = requests.get(
            f"https://blockchain.info/q/addressbalance/{self.address}")
        # Convert from sats to btc (/100000000)
        return int(response.json()) / 100000000

    def get_current_balance_fiat(self, currency) -> float:
        """
        Returns the fiat value of the amount of bitcoin currently in a given wallet.

        Parameters:
        btc_address (str): The bitcoin wallet to get amount from.
        currency (str): The currency to provide value in.

        Returns:
        (float): Fiat amount of bitcoin in given wallet.
        """
        response = requests.get(
            f"https://api.coindesk.com/v1/bpi/currentprice.json")
        current_val = float(response.json()["bpi"][currency.upper()]['rate'].replace(',', ''))
        return round(current_val * self.get_current_balance(), 2)

    def get_first_seen(self) -> datetime:
        """
        Returns the timestamp of the block an address was first confirmed in.

        Parameters:
        address (str): The bitcoin wallet.

        Returns:
        (datetime): The date the block an address was first confirmed in.
        """
        response = requests.get(
            f"https://blockchain.info/q/addressfirstseen/{self.address}")
        return datetime.fromtimestamp(response.json())

    def get_transaction_count(self) -> int:
        """
        Returns the number of transactions associated with a wallet.

        Parameters:
        address (str): The bitcoin wallet.

        Returns:
        (int): The number of transactions.
        """
        response = requests.get(
            f"https://blockchain.info/rawaddr/{self.address}")
        return response.json()["n_tx"]

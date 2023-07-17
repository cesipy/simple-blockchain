from transaction import Transaction
from wallet import Wallet
import random


def create_wallets(number_wallets: int, blockchain) -> [Wallet]:
    """
    creates 'number_wallets' wallets and returns a list of those wallets.
    this can be used to simulate transactions on the blockchain
    """
    wallets = []
    for i in range(number_wallets):
        new_wallet = Wallet(i, blockchain,  random.uniform(1.0, 100.0))
        wallets.append(new_wallet)

    return wallets


def simulate_transactions(amount_interactions: int, wallet_list: [Wallet]) -> [Transaction]:
    """
    simulate an amount of transactions and return a list of transactions
    """
    counter = 0
    transaction_list = []

    while counter < amount_interactions:
        sender = wallet_list[random.randint(0, len(wallet_list) - 1)]
        recipient = wallet_list[random.randint(0, len(wallet_list) - 1)]

        while sender == recipient or sender.get_balance() < 0.005:
            sender = wallet_list[random.randint(0, len(wallet_list) - 1)]

        amount = min(sender.get_balance(), random.uniform(0.001, sender.get_balance()))
        transaction = sender.send(recipient, amount)
        transaction_list.append(transaction)
        counter += 1

    return transaction_list

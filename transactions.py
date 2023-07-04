from transaction import Transaction
from wallet import Wallet
import random


def create_wallets(number_wallets: int) -> [Wallet]:
    wallets = []
    for i in range(number_wallets):
        new_wallet = Wallet(i, random.uniform(1.0, 100.0))
        wallets.append(new_wallet)

    return wallets


def simulate_transactions(amount_interactions: int, wallet_list: [Wallet]) -> [Transaction]:
    counter = 0
    transaction_list = []

    while counter < amount_interactions:
        sender = wallet_list[random.randint(0, len(wallet_list) - 1)]
        recipient = wallet_list[random.randint(0, len(wallet_list) - 1)]

        while sender == recipient:
            recipient = wallet_list[random.randint(0, len(wallet_list) - 1)]

        amount = random.uniform(0.001, sender.get_balance())
        transaction = sender.send(recipient, amount)
        transaction_list.append(transaction)
        counter += 1

    return transaction_list

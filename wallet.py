from transaction import Transaction


class Wallet:
    def __init__(self, address: int, balance=0):
        self.address = address
        self.balance = balance  # balance in constructor only used for testing! should be removed

    def send(self, recipient_wallet, amount: float) -> Transaction:
        """
        sends a transaction from the calling wallet to a recipient wallet
        if there is not enough balance, the method raises an exception
        """
        if self.balance < amount:
            raise ValueError(f"Wallet {self.address} does not have enough balance. Available balance: {self.balance}")

        recipient_wallet.update_balance(amount)
        self.balance -= amount
        print(f"Wallet {self.address} sent {amount} to Wallet {recipient_wallet.address}")

        transaction = Transaction(self, recipient_wallet, amount)
        return transaction

    def get_balance(self):
        return self.balance

    def update_balance(self, amount):
        self.balance += amount

    def __repr__(self) -> str:
        return f"Wallet:\n\taddress: {self.address}\n\t" \
               f"balance: {self.balance}\n"

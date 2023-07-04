class Wallet:
    def __init__(self, address):
        self.address = address
        self.balance = 0

    def send_transaction(self, recipient_wallet, amount: int) -> bool:
        """
        sends a transaction from the calling wallet to a recipient wallet
        if there is not enough balance, the method return false
        """
        if self.balance < amount:
            print(f"Wallet {self.address} does not have enough balance")
            return False

        recipient_wallet.update_balance(amount)
        self.balance -= amount
        print(f"Wallet {self.address} sent {amount} to Wallet {recipient_wallet.address}")

        return True

    def get_balance(self):
        return self.balance

    def update_balance(self, amount):
        self.balance += amount

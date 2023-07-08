class Transaction:

    def __init__(self, sender, recipient, amount: float):  # ,transaction_id: int):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        # self.id = transaction_id

    def __repr__(self):
        ret = f"Transaction:\n \t" \
              f"Sender:    {self.sender}\n\t" \
              f"Recipient: {self.recipient}\n\t" \
              f"amount:    {self.amount}\n"
        return ret

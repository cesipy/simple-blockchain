class Transaction:
    
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __repr__(self):
        ret = f"Transaction\n: \tSender {self.sender}\n\tRecipient {self.recipient}\n\tamount: {self.amount}\n"
        return ret
    
    
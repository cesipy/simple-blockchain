import random


class Transaction:

    def __init__(self, sender, recipient, amount, transaction_id):
        self.sender    = sender
        self.recipient = recipient
        self.amount    = amount
        self.id        = transaction_id

    def __repr__(self):
        ret = f"Transaction:\n \t" \
              f"Sender:    {self.sender}\n\t" \
              f"Recipient: {self.recipient}\n\t" \
              f"amount:    {self.amount}\n"
        return ret


def simulate_transactions(amount_transactions: int) -> [Transaction]:
    counter = 0
    transaction_list = []
    while counter < amount_transactions:
        # create a random sender, recipient and amount
        randomized_sender = random.randint(1000, 9999)  # exchange with wallet constructor afterward
        randomized_recipient = random.randint(1000, 9999)
        randomized_amount = random.random()

        while randomized_sender == randomized_recipient:
            randomized_recipient = random.randint(1000, 9999)

        # create transaction based on the random data
        transaction = Transaction(randomized_sender, randomized_recipient, randomized_amount, counter+1)
        transaction_list.append(transaction)

        counter += 1

    return transaction_list


# testing the transaction class:
def testing():
    transaction1 = Transaction(123, 899, 0.01, 1234)
    print(transaction1)

    transaction_list = simulate_transactions(19)
    print(transaction_list)


testing()

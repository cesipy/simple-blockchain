import block

import transactions
import wallet

DIFF = 1  # change if you want faster block creation


def test_hash_function():
    print("hash function:")
    genesis_block = block.create_first_block(DIFF)
    print(block.calculate_hash(genesis_block))


# testing the transaction class:
def test_transactions():
    print("transactions:")
    wallet1 = wallet.Wallet(12, balance=12)
    wallet2 = wallet.Wallet(11)
    transaction1 = transactions.Transaction(123, 899, 0.01)
    print(transaction1)

    wallet_list = transactions.create_wallets(4)
    transaction_list = transactions.simulate_transactions(19, wallet_list)
    print(transaction_list)


def test_wallet():
    print("wallets:")
    wallet1 = wallet.Wallet(12, balance=12)
    wallet2 = wallet.Wallet(11)

    print(wallet1, wallet2)

    # transactions
    wallet1.send(wallet2, 0.15)
    print("after transaction:")
    print(wallet1, wallet2)

    # wallet2.send(wallet1, 1)


def main():
    print("main functionality:")
    # generate genesis block
    genesis_block = block.create_first_block(DIFF)
    previous_block = genesis_block
    print(previous_block, '\n')

    # create
    for i in range(100):
        current_block = block.create_next_block(previous_block)
        print(current_block, '\n')
        previous_block = current_block


if __name__ == '__main__':
    # test_wallet()
    # print("testing: ")
    # test_hash_function()
    # test_transactions()
    main()

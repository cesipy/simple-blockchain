import block
import hash_function
import transactions

DIFF = 3  # change if you want faster block creation


def test_hash_function():
    print("hash function:")
    genesis_block = block.create_first_block(DIFF)
    print(hash_function.calculate_hash(genesis_block))


# testing the transaction class:
def test_transactions():
    print("transactions:")
    transaction1 = transactions.Transaction(123, 899, 0.01, 1234)
    print(transaction1)

    transaction_list = transactions.simulate_transactions(19)
    print(transaction_list)


def main():
    print("main functionality:")
    # generate genesis block
    genesis_block = block.create_first_block(DIFF)
    previous_block = genesis_block
    print(previous_block, '\n')

    # create
    for i in range(5):
        current_block = block.create_next_block(previous_block)
        print(current_block, '\n')
        previous_block = current_block


if __name__ == '__main__':
    print("testing: ")
    test_hash_function()
    test_transactions()
    main()

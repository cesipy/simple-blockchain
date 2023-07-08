import hash_function
from blockchain import Blockchain
import transactions
import wallet
from miner import Miner
from threading import Thread

DIFF = 2  # change if you want faster block creation


def test_hash_function():
    print("hash function:")
    blockchain = Blockchain(DIFF)
    genesis_block = blockchain.create_first_block()
    print(hash_function.calculate_hash(genesis_block))


# testing the transaction class:
def test_transactions():
    print("transactions:")
    blockchain = Blockchain(DIFF)
    # wallet1 = wallet.Wallet(12, blockchain, balance=12)
    # wallet2 = wallet.Wallet(11, blockchain)
    transaction1 = transactions.Transaction(123, 899, 0.01)
    print(transaction1)

    wallet_list = transactions.create_wallets(4, blockchain)
    transaction_list = transactions.simulate_transactions(19, wallet_list)
    print(transaction_list)


def test_wallet():
    print("wallets:")
    blockchain = Blockchain(DIFF)
    wallet1 = wallet.Wallet(12, blockchain, balance=12)
    wallet2 = wallet.Wallet(11, blockchain)

    print(wallet1, wallet2)

    # transactions
    wallet1.send(wallet2, 0.15)
    print("after transaction:")
    print(wallet1, wallet2)

    # wallet2.send(wallet1, 1)


def test_blockchain_class():
    print("blockchain:")
    blockchain = Blockchain(DIFF)

    genesis_block = blockchain.create_first_block()
    blockchain.add_block(genesis_block)
    previous_block = genesis_block

    for i in range(5):
        current_block = blockchain.create_next_block(previous_block)
        blockchain.add_block(current_block)
        previous_block = current_block

    blockchain.save_to_file("blockchain.txt")


def test_single_miner():
    print("main functionality:")
    # generate genesis block
    blockchain = Blockchain(DIFF)
    genesis_block = blockchain.create_first_block()
    blockchain.add_block(genesis_block)
    previous_block = genesis_block
    print(previous_block, '\n')

    # create
    for i in range(100):
        current_block = blockchain.create_next_block(previous_block)
        blockchain.add_block(current_block)
        print(current_block, '\n')
        previous_block = current_block

    blockchain.save_to_file('blockchain.txt')


def test_main(number_threads):
    blockchain = Blockchain(DIFF)

    genesis_block = blockchain.create_first_block()
    blockchain.add_block(genesis_block)

    # miners
    miners = [Miner(i, blockchain, 100) for i in range(number_threads)]

    threads = []
    for miner in miners:
        miner_thread = Thread(target=miner.mine)
        miner_thread.start()
        threads.append(miner_thread)

    # make main thread wait for all miner threads to finish
    for thread in threads:
        thread.join()

    # print out all the blocks in the blockchain
    for block in blockchain.blocks:
        print(block)

    for miner in miners:
        print(miner)

    blockchain.save_to_file("blockchain.txt")


if __name__ == '__main__':
    # test_blockchain_class()
    # test_wallet()
    # test_hash_function()
    # test_transactions()
    test_main(10)

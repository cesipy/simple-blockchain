import random
import threading
import time

import metadata
import transactions
from block import Block
import hash_function

RANGE = 1234
AMOUNT_TRANSACTIONS_IN_BLOCK = 100


def proof_of_work(block: Block) -> Block:
    difficulty = block.metadata.difficulty

    trying_hash = hash_function.calculate_hash(block)  # is first computed hash a valid hash
    difficulty_compare = '0' * difficulty  # essentially '00...' - amount of leading zeros

    # use bruteforce to find valid hash
    while (trying_hash[0:difficulty] != difficulty_compare):
        block.nonce += 1
        trying_hash = hash_function.calculate_hash(
            block)
    block.hash = trying_hash

    return block


class Blockchain:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blocks = []
        self.current_block_available = True
        self.lock = threading.Lock()
        self.candidate_block = None
        self.block_counter = 0

    def add_block(self, block):
        """
        add block 'block' to the blockchain.
        """
        self.blocks.append(block)

    def save_to_file(self, file_path):
        """
        save the current state of the blockchain in the file specified by 'file_path'.
        """
        with open(file_path, 'w') as f:
            for block in self.blocks:
                f.write(str(block) + '\n')

    def create_first_block(self) -> Block:
        """
        creates genesis block. simulates transactions and adds transaction list to block
        """
        rewards = 6.5
        block_number = 1
        difficulty = self.difficulty  # fetch difficulty of blockchain and save in metadata
        meta = metadata.Metadata(difficulty, 1.0, rewards, block_number)

        # simulate a list of transactions
        wallet_list = transactions.create_wallets(21, self)  # self...the blockchain is given to the transactions list
        transaction_list = transactions.simulate_transactions(AMOUNT_TRANSACTIONS_IN_BLOCK, wallet_list)
        block = Block("0", 0, transaction_list, meta)

        # update the candidate block for next block
        self.candidate_block = self.create_candidate(block)

        # returning the genesis block
        return block

    def add_next_block(self, block):
        """
        updates the current state of the blockchain. 'block' is added to the blockchain and the counter for the number
        of blocks in blockchain is updated. blockchain gets updated, that no current block is available.
        """
        self.add_block(block)
        self.block_counter += 1
        self.current_block_available = False

    def start_new_iteration(self, block):
        """
        new block is available. a new block candidate is created and flag is set, indicating a new block is available
        for miners.
        """
        self.candidate_block = self.create_candidate(block)

        self.current_block_available = True

    def create_candidate(self, previous_block: Block) -> Block:
        """
        create block candidate for mining. is spread out to all the miners, to work on proof of work
        """
        difficulty, version, rewards, block_number = previous_block.metadata.get_params()

        block_number += 1
        meta = metadata.Metadata(difficulty, version, rewards, block_number)
        new_nonce = random.randint(1, RANGE)

        wallet_list = transactions.create_wallets(21, self)
        transaction_list = transactions.simulate_transactions(AMOUNT_TRANSACTIONS_IN_BLOCK, wallet_list)
        block = Block(previous_block.hash, new_nonce, transaction_list, meta)

        return block

    def get_update(self):
        """
         fetches current information of the blockchain and returns block counter as well the flag if
         current block is already mined or not (bool)
        """
        self.lock.acquire()
        counter = self.block_counter
        available = self.current_block_available
        self.lock.release()

        return counter, available

    def create_next_block(self, previous_block: Block) -> Block:
        """
        creates next block given the previous block.
        simulates transactions and adds list of transactions to block. at the end, proof of work is called,
        to use computation making it more secure.

        only used, if there are no miners.
        """
        metadata_from_prev = previous_block.metadata
        # get all the parameter for metadata from prev block
        difficulty, version, rewards, block_number = metadata_from_prev.get_params()

        block_number += 1
        meta = metadata.Metadata(difficulty, version, rewards, block_number)

        new_nonce = random.randint(1, RANGE)

        # simulate list of transactions
        wallet_list = transactions.create_wallets(21, self)
        transaction_list = transactions.simulate_transactions(AMOUNT_TRANSACTIONS_IN_BLOCK, wallet_list)
        block = Block(previous_block.hash, new_nonce, transaction_list, meta)

        return proof_of_work(block)

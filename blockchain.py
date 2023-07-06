import random
import metadata
import transactions
from block import Block
import hash_function

RANGE = 1234
AMOUNT_TRANSACTIONS_IN_BLOCK = 100



class Blockchain:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blocks = []

    def add_block(self, block):
        self.blocks.append(block)

    def save_to_file(self, file_path):
        with open(file_path, 'w') as f:
            for block in self.blocks:
                f.write(str(block) + '\n')

    def create_first_block(self) -> Block:
        rewards = 6.5
        block_number = 1
        difficulty = self.difficulty            # fetch difficulty of blockchain and save in metadata
        meta = metadata.Metadata(difficulty, 1.0, rewards, block_number)

        # simulate a list of transactions
        wallet_list = transactions.create_wallets(21, self)     #self...the blockchain is given to the transactions list
        transaction_list = transactions.simulate_transactions(AMOUNT_TRANSACTIONS_IN_BLOCK, wallet_list)
        block = Block("0", 0, transaction_list, meta)
        return block

    # add create first block and next block to blockchain class. so that transactions and wallets can be simulated

    def create_next_block(self, previous_block: Block) -> Block:
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

        return self.proof_of_work(block)

    def proof_of_work(self, block: Block) -> Block:
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

    def create_candidate(self, previous_block: Block) -> Block:
        """
        create block candidate for mining
        """
        difficulty, version, rewards, block_number = previous_block.metadata.get_params()

        block_number += 1
        meta = metadata.Metadata(difficulty, version, rewards, block_number)
        new_nonce = random.randint(1, RANGE)

        wallet_list = transactions.create_wallets(21)
        transaction_list = transactions.simulate_transactions(AMOUNT_TRANSACTIONS_IN_BLOCK, wallet_list)
        block = Block(previous_block.hash, new_nonce, transaction_list, meta)

        return block

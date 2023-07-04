import time
import hash_function
import metadata
import random

RANGE = 1234


class Block:
    def __init__(self, prev_hash, nonce, transactions, meta_data):
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.nonce = nonce
        self.hash = hash_function.calculate_hash(
            self)  # hash is calculated, so does not need to be passed in constructor
        self.transactions = transactions
        self.metadata = meta_data

    def __repr__(self):
        return f"Block {self.metadata.block_number}: {self.hash} from {self.timestamp}"


def create_first_block(difficulty: int) -> Block:
    rewards = 6.5
    block_number = 1
    meta = metadata.Metadata(difficulty, 1.0, rewards, block_number)
    block = Block("0", 0, [], meta)
    return block


def create_next_block(previous_block: Block) -> Block:
    metadata_from_prev = previous_block.metadata
    # get all the parameter for metadata from prev block
    difficulty, version, rewards, block_number = metadata_from_prev.get_params()
    block_number += 1
    meta = metadata.Metadata(difficulty, version, rewards, block_number)

    new_nonce = random.randint(1, RANGE)
    block = Block(previous_block.hash, new_nonce, [], meta)

    return proof_of_work(block)


def proof_of_work(block: Block) -> Block:
    difficulty = block.metadata.difficulty

    trying_hash = hash_function.calculate_hash(
        block)  # is first computed hash a valid hash
    difficulty_compare = '0' * difficulty  # essentially '00...' - amount of leading zeros

    # use bruteforce to find valid hash
    while (trying_hash[0:difficulty] != difficulty_compare):
        block.nonce += 1
        trying_hash = hash_function.calculate_hash(
            block)
    block.hash = trying_hash

    return block

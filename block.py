import time
import hash_function
import metadata
import random
import transactions
import hashlib

RANGE = 1234
AMOUNT_TRANSACTIONS_IN_BLOCK = 100


class Block:
    def __init__(self, prev_hash, nonce, transaction_list, meta_data):
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.nonce = nonce
        self.hash = hash_function.calculate_hash(
            self)  # hash is calculated, so does not need to be passed in constructor
        self.transactions = transaction_list
        self.metadata = meta_data

    def __repr__(self):
        return f"Block {self.metadata.block_number}: {self.hash} from {self.timestamp}"


def create_first_block(difficulty: int) -> Block:
    rewards = 6.5
    block_number = 1
    meta = metadata.Metadata(difficulty, 1.0, rewards, block_number)

    # simulate a list of transactions
    wallet_list = transactions.create_wallets(21)
    transaction_list = transactions.simulate_transactions(AMOUNT_TRANSACTIONS_IN_BLOCK, wallet_list)
    block = Block("0", 0, transaction_list, meta)
    return block


def create_next_block(previous_block: Block) -> Block:
    metadata_from_prev = previous_block.metadata
    # get all the parameter for metadata from prev block
    difficulty, version, rewards, block_number = metadata_from_prev.get_params()
    block_number += 1
    meta = metadata.Metadata(difficulty, version, rewards, block_number)

    new_nonce = random.randint(1, RANGE)

    # simulate list of transactions
    wallet_list = transactions.create_wallets(21)
    transaction_list = transactions.simulate_transactions(AMOUNT_TRANSACTIONS_IN_BLOCK, wallet_list)
    block = Block(previous_block.hash, new_nonce, transaction_list, meta)

    return proof_of_work(block)


def proof_of_work(block: Block) -> Block:
    difficulty = block.metadata.difficulty

    trying_hash = calculate_hash(block)  # is first computed hash a valid hash
    difficulty_compare = '0' * difficulty  # essentially '00...' - amount of leading zeros

    # use bruteforce to find valid hash
    while (trying_hash[0:difficulty] != difficulty_compare):
        block.nonce += 1
        trying_hash = hash_function.calculate_hash(
            block)
    block.hash = trying_hash

    return block


def calculate_hash(current_block: Block) -> str:
    meta_data = f"{current_block.prev_hash} plus {current_block.timestamp} plus {current_block.nonce}"
    h = hashlib.blake2b()  # create hash object
    h.update(meta_data.encode())
    time.sleep(0.001)
    return h.hexdigest()

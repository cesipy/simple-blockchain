import time
import hash_function

RANGE = 1234
AMOUNT_TRANSACTIONS_IN_BLOCK = 100


class Block:
    def __init__(self, prev_hash, nonce, transaction_list, meta_data):
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.nonce = nonce
        self.hash = hash_function.calculate_hash(self) #hash is calculated, so does not need to be passed in constructor
        self.transactions = transaction_list
        self.metadata = meta_data

    def __repr__(self):
        return f"Block {self.metadata.block_number}: {self.hash} from {self.timestamp}"

    '''def hash(self):
        hash_function.calculate_hash(self)
'''

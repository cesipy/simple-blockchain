import time
import hash_function
import metadata

class Block:
    def __init__(self, prev_hash,  nonce, hash, transactions, metadata):
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.nonce = nonce
        self.hash = hash
        self.transactions = transactions
        self.metadata = metadata

    def __repr__(self):
        return f"Block : {self.hash} from {self.timestamp}"
    

def create_first_block(difficulty):
    meta = metadata.Metadata(difficulty, 1.0, 6.5)
    block =  Block("0", 0, "hash", [], meta)
    return block


def proof_of_work(block):
    difficulty = block.metadata.difficulty       
    current_nonce = block.nonce

    trying_hash = hash_function.calculate_hash(
        block, current_nonce)    # is first computed hash a valid hash
    difficulty_compare = '0' * difficulty    # essentially '00...' - amount of leading zeros

    # use bruteforce to find valid hash
    while (trying_hash[0:difficulty] != difficulty_compare):
        current_nonce+= 1
        trying_hash = hash_function.calculate_hash(
            block, current_nonce)

    return trying_hash
    
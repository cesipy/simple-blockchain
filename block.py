import time
import hash_function

class Block:
    def __init__(self, prev_hash,  nonce, hash, transactions, difficulty):
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.nonce = nonce
        self.hash = hash
        self.transactions = transactions
        self.difficulty = difficulty

    def __repr__(self):
        return f"Block : {self.hash} from {self.timestamp}"
    

def create_first_block(difficulty):
    block =  Block("0", 0, "hash", [], difficulty)
    return block


def proof_of_work(block):
    difficulty = block.difficulty       
    current_nonce = block.nonce

    trying_hash = hash_function.calculate_hash(block, current_nonce)    # is first computed hash a valid hash
    difficulty_compare = '0' * difficulty                         # essentially '00...' - amount of leading zeros

    # use bruteforce to find valid hash
    while (trying_hash[0:difficulty] != difficulty_compare):
        current_nonce+= 1
        trying_hash = hash_function.calculate_hash(block, current_nonce)

    return trying_hash
    
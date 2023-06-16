import time
import hash_function
import metadata
import random

RANGE = 1234

class Block:
    def __init__(self, prev_hash,  nonce, transactions, metadata):
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.nonce = nonce
        self.hash = hash_function.calculate_hash(self, self.nonce)      # hash is calculated, so does not need to be passed in contructor
        self.transactions = transactions        
        self.metadata = metadata

    def __repr__(self):
        return f"Block : {self.hash} from {self.timestamp}"
    

def create_first_block(difficulty):
    meta = metadata.Metadata(difficulty, 1.0, 6.5)
    block =  Block("0", 0,  [], meta)
    return block

def create_next_block(previous_block):
    '''
    TODO:
        - create new hash
        - calculate new nonce (maybe random)
        - simulate transactions
        - update metadata if a counter is reachd (ex.: increase difficulty)
        - do the proof of work
    
    '''
    meta = previous_block.metadata
    new_nonce = random.randint(1, RANGE)
    block = Block(previous_block.hash, new_nonce, [], meta)

    return proof_of_work(block)


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
    
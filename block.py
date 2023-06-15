import time

class Block:
    def __init__(self, prev_hash,  nonce, hash, transactions):
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.nonce = nonce
        self.hash = hash
        self.transactions = transactions

    def __repr__(self):
        return "Block : %s from %s", self.hash, self.timestamp
    


def create_first_block():
    
    block =  Block("0", 0, "hash", [])
    print(block)
    return block
import block, hashlib

def calculate_hash(block):
    meta_data = f"{block.hash} plus {block.timestamp} plus {block.nonce}"
    h = hashlib.blake2b()     #create hash object
    h.update(meta_data.encode())
    return h.hexdigest()


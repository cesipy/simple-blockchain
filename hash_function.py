import block, hashlib, time

def calculate_hash(block):
    meta_data = f"{block.prev_hash} plus {block.timestamp} plus {block.nonce}"
    h = hashlib.blake2b()     #create hash object
    h.update(meta_data.encode())
    time.sleep(0.001)
    return h.hexdigest()


import block
import hashlib
import time


def calculate_hash(current_block: block) -> str:
    meta_data = f"{current_block.prev_hash} plus {current_block.timestamp} plus {current_block.nonce}"
    h = hashlib.blake2b()  # create hash object
    h.update(meta_data.encode())
    time.sleep(0.001)
    return h.hexdigest()

import wallet
from blockchain import proof_of_work


class Miner(wallet.Wallet):

    def __init__(self, address, blockchain, balance=0):
        super().__init__(address, blockchain, balance)
        self.lock = blockchain.lock
        self.counter = blockchain.block_counter
        self.running = True

    def mine(self):
        """
        miner competes with other miners using this function.
        each miner gets the candidate block (processed by blockchain)
        and tries to solve PoW.

        winning miner gets reward specified in block header.
        """
        while self.counter < 10:

            self.counter, available = self.blockchain.get_update()
            self.blockchain.lock.acquire()
            self.counter = self.blockchain.block_counter  # update counter
            if available:
                block = self.blockchain.candidate_block

                self.blockchain.lock.release()

                mined_block = proof_of_work(block)

                self.blockchain.lock.acquire()

                # if counter differ -> another miner finished first
                if self.blockchain.block_counter == self.counter and self.blockchain.current_block_available:
                    # print(f"Miner {self.address} successfully added block {mined_block}")
                    self.blockchain.add_next_block(mined_block)
                    self.blockchain.start_new_iteration(mined_block)

                self.blockchain.lock.release()

            else:

                self.blockchain.lock.release()

            # simulate additional work load
            #time.sleep(2)
            # update variables for next iteration
            self.counter, available = self.blockchain.get_update()

    def stop(self):
        self.running = False

    def __repr(self):
        return f"Miner {self.address}: balance: {self.balance}"

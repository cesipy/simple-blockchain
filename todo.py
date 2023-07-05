'''
TODO:
    - add block number in metadata              √
    - add type definition to all functions      √
    - improve code with better OOP principles (classes, methods)


    - transactions
        - class of transactions                 √
        - random transactions simulator         √
        - own function to create a list of transactions
        that will be added to the next block    √
        - add transactions at block creation    √
        - validate transactions

    - Add a public ledger that multiple 'miners' can work on the project
        - Create a Blockchain class to manage multiple blocks
        - Implement method to save the blockchain to a file
        - Implement method to read the blockchain from a file

    - Wallets
        - Implement Wallet class
        - Add balance checking in transaction validation
        - Simulate mining rewards being added to miner's wallet

    - Network simulation
        - Implement Node class to simulate network nodes
        - Create multiple Node instances in different threads to simulate network
        - When a node creates a transaction, broadcast to all other nodes (pending transactions pool)
        - When a node mines a new block, broadcast it to all other nodes
        - Implement consensus algorithm to handle conflicts when different nodes mine new blocks

    - Other enhancements
        - Implement periodic difficulty adjustment based on how quickly blocks are being mined
        - Add more transaction types (eg. contract creation, contract execution)
'''

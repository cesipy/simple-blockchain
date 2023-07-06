'''
TODO:
    quick:
    - showcase program without miners
    - docstring for all (important) methods
    - refactor and merge
    - miner should get reward (on blockchain)
    - miner info stored in metadata (also include
    in create_first_block, create_next_block)


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
        - Implement Wallet class                                √
        - Add balance checking in transaction validation        √
        - Simulate mining rewards being added to miner's wallet √

    - Network simulation
        - Implement Node class to simulate network nodes
        - Create multiple Node instances in different threads to simulate network
        - When a node creates a transaction, broadcast to all other nodes (pending transactions pool)
        - When a node mines a new block, broadcast it to all other nodes
        - Implement consensus algorithm to handle conflicts when different nodes mine new blocks

    - Other enhancements
        - Implement periodic difficulty adjustment based on how quickly blocks are being mined
        - Add more transaction types (eg. contract creation, contract execution)

    - Implement P2P Networking
        - Create a P2P network of nodes using libraries like socket or asyncio
        - Define protocols for nodes to connect, disconnect, send and receive messages

    - Modify Wallet and Block classes for network operations
        - Modify Wallet's send() method to broadcast transactions to all connected nodes
        - Modify proof_of_work() method to broadcast new block to all connected nodes

    - Blockchain Consensus Protocol
        - Implement a protocol to handle conflicts (when nodes have different versions of the blockchain)

    - Persistency
        - Save blockchain data to disk periodically
        - Load blockchain data from disk at startup

    - Security Measures
        - Implement transaction verification to prevent double-spending
        - Validate mined blocks before adding them to the blockchain'''

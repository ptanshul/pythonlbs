import datetime
import hashlib

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(
            str(self.index).encode() +
            str(self.timestamp).encode() +
            str(self.data).encode() +
            str(self.previous_hash).encode()
        ).hexdigest()
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
                if current_block.hash != current_block.calculate_hash():
                    return False
                if current_block.previous_hash != previous_block.hash:
                    return False
            return True
    # Create a blockchain
my_blockchain = Blockchain()

# Add new blocks
my_blockchain.add_block(Block(1, datetime.datetime.now(), "Transaction Data", ""))
my_blockchain.add_block(Block(2, datetime.datetime.now(), "Another Transaction", ""))

# Check if the blockchain is valid
print("Is blockchain valid?", my_blockchain.is_chain_valid())

# Manipulate the chain (tampering with data)
my_blockchain.chain[1].data = "Manipulated Data"

# Recheck validity after manipulation
print("Is blockchain valid after manipulation?", my_blockchain.is_chain_valid())

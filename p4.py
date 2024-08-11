import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    @staticmethod
    def calculate_hash(index, previous_hash, timestamp, data):
        value = str(index) + previous_hash + str(timestamp) + str(data)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    @staticmethod
    def create_genesis_block():
        return Block(0, "0", int(time.time()), "Genesis Block", Block.calculate_hash(0, "0", int(time.time()), "Genesis Block"))

    def __str__(self):
        return f"Block #{self.index} [previous_hash: {self.previous_hash}, hash: {self.hash}, data: {self.data}]"

class Blockchain:
    def __init__(self):
        self.chain = [Block.create_genesis_block()]

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_index = latest_block.index + 1
        new_timestamp = int(time.time())
        new_hash = Block.calculate_hash(new_index, latest_block.hash, new_timestamp, data)
        new_block = Block(new_index, latest_block.hash, new_timestamp, data, new_hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is valid
            if current_block.hash != Block.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False

            # Check if the current block points to the correct previous block
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def __str__(self):
        chain_str = ""
        for block in self.chain:
            chain_str += str(block) + "\n"
        return chain_str

# Create a blockchain and add some blocks
blockchain = Blockchain()
print("Genesis block created:")
print(blockchain)

blockchain.add_block("First Block after Genesis")
blockchain.add_block("Second Block after Genesis")
blockchain.add_block("Third Block after Genesis")

print("Blockchain after adding blocks:")
print(blockchain)

# Check if the blockchain is valid
print("Is blockchain valid?", blockchain.is_chain_valid())

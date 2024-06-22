import hashlib

class FATCoinBlock:
  def __init__(self, previous_block_hash, transaction_list):
    self.previous_block_hash = previous_block_hash
    self.transaction_list = transaction_list

    self.block_data = "*".join(transaction_list) + "*" + previous_block_hash
    self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Anna sends 2 FC to Mike"
t2 = "Bob sends 4.1 FC to Daniel"
t3 = "Mike sends 3.2 FC to George"
t4 = "Daniel sends 0.3 FC to Bob"
t5 = "Mike sends 1 FC to Anna"
t6 = "George sends 5.4 FC to Mike"

initial_block = FATCoinBlock("Initial Block String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = FATCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = FATCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)
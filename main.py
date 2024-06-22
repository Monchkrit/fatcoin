import hashlib

NONCE_LIMIT = 100000000000000000000

zeroes = 4

def fatmine(block_number, transactions, previous_hash):
  for nonce in range (NONCE_LIMIT):
    base_text = str(block_number) + transactions + previous_hash + str(nonce)
    hash_try = hashlib.sha256(base_text.encode()).hexdigest()
    if hash_try.startswith('0' * zeroes):
      print(f"Found Hash With Nonce: {nonce}")
      return hash_try
    
  return -1
  
block_number = 24
transactions = "76123fcc2142"
previous_hash = "876de8756b967c87"

fatmine(block_number, transactions, previous_hash)
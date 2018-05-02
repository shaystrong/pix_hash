import hashlib as hasher
import datetime as date
from PIL import Image
import numpy as np

#based on https://gist.github.com/aunyks/47d157f8bc7d1829a729c2a6a919c173

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = np.array(Image.open('data/taco_cat.jpg'))
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
  def hash_block(self):
    sha = hasher.sha256()
    sha.update((str(self.index) + 
               str(self.timestamp) + 
               str(self.data) + 
               str(self.previous_hash)).encode('utf-8'))
    return sha.hexdigest()

def create_genesis_block():
  return Block(0, date.datetime.now(), 'Genesis Block', '0')

def next_block(last_block,data):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = data
  this_hash = last_block.hash
  return Block(this_index, this_timestamp, this_data, this_hash)

# Create the blockchain and add the 'genesis' block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]
data2=np.array(Image.open('data/pizza_cat.jpg'))

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 10

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block,data2)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  # Tell everyone about it!
  print ('Block #{} has been added to the chain'.format(block_to_add.index))
  print ('Hash: {}\n'.format(block_to_add.hash) )

## mining

miner_address = 'q3nf394hjg-random-miner-address-34nf3i4nflkn3oi'

def proof_of_work(last_proof):
  # Create a variable that we will use to find
  # our next proof of work
  incrementor = last_proof + 1
  # Keep incrementing the incrementor until
  # it's equal to a number divisible by 9 and the proof of work of the previous
  # block in the chain
  while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
    incrementor += 1
  # Once that number is found,
  # we can return it as a proof
  # of our work
  return incrementor

@node.route('/mine', methods = ['GET'])
def mine():
  # Get the last proof of work
  last_block = blockchain[len(blockchain) - 1]
  last_proof = last_block.data['proof-of-work']
  # Find the proof of work for
  # the current block being mined
  # Note: The program will hang here until a new
  #       proof of work is found
  proof = proof_of_work(last_proof)
  # Once we find a valid proof of work,
  # we know we can mine a block so 
  # we reward the miner by adding a transaction
  this_nodes_transactions.append(
    { 'from': 'network', 'to': miner_address, 'amount': 1 }
  )
  # Now we can gather the data needed
  # to create the new block
  new_block_data = {
    'proof-of-work': proof,
    'transactions': list(this_nodes_transactions)
  }
  new_block_index = last_block.index + 1
  new_block_timestamp = this_timestamp = date.datetime.now()
  last_block_hash = last_block.hash
  # Empty transaction list
  this_nodes_transactions[:] = []
  # Now create the
  # new block!
  mined_block = Block(
    new_block_index,
    new_block_timestamp,
    new_block_data,
    last_block_hash
  )
  blockchain.append(mined_block)
  # Let the client know we mined a block
  return json.dumps({
      'index': new_block_index,
      'timestamp': str(new_block_timestamp),
      'data': new_block_data,
      'hash': last_block_hash
  }) + '\n'
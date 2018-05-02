import hashlib as hasher
import datetime as date
from PIL import Image
import numpy as np

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
  return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block,data):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = data
  this_hash = last_block.hash
  return Block(this_index, this_timestamp, this_data, this_hash)

# Create the blockchain and add the genesis block
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
  print ("Block #{} has been added to the blockchain".format(block_to_add.index))
  print ("Hash: {}\n".format(block_to_add.hash) )
  

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib
import time


# In[30]:


class Block:
    def __init__(self):
        self.chain = []
    def create_block(self, index, previous_hash, timestamp, data, hash):
        block = {
            "index": index,
            "previous_hash": previous_hash,
            "timestamp": timestamp,
            "data": data,
            "hash": hash,
        }
        self.chain.append(block)


# In[39]:


class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + previous_hash + str(timestamp) + data
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    index = 0
    previous_hash = "0"
    timestamp = int(time.time())
    data = "Genesis Block"
    hash_value = calculate_hash(index, previous_hash, timestamp, data)
    return Block(index, previous_hash, timestamp, data, hash_value)

genesis_block = create_genesis_block()


# In[40]:


def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)


# In[41]:


blockchain = [create_genesis_block()]
previous_block = blockchain[0]


# In[42]:


data = """
TransactionNo :581482  Date;12-09-2019  ProductNo:22485  ProductName:Set Of 2 Wooden Market Crates       Price:21.47 Quantity:12  CustomerNo:17490  Country:UK
TransactionNo :581475  Date:12-09-2019  ProductNo:22596  ProductName:Christmas Star Wish List Chalkboard Price:10.65 Quantity:36  CustomerNo:13069  Country:UK
TransactionNo :581475  Date:12-09-2019  ProductNo:23235  ProductName:Storage Tin Vintage Leaf            Price:11.53 Quantity:12  CustomerNo:13069  Country:UK
TransactionNo :581475  Date:12-09-2019  ProductNo:23272  ProductName:Tree T-Light Holder Willie Winkie   Price:10.65 Quantity:12  CustomerNo:13069  Country:UK
TransactionNo :581475  Date:12-09-2019  ProductNo:23239  ProductName:Set Of 4 Knick Knack Tins Poppies   Price:11.94 Quantity:6   CustomerNo:13069  Country:UK
"""


# In[43]:


transactions = data.strip().split("\n")


# In[44]:


for transaction in transactions:
    new_block = create_new_block(previous_block, transaction)
    blockchain.append(new_block)
    previous_block = new_block


# In[45]:


for block in blockchain:
    print(f"Block #{block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("\n")


# In[ ]:





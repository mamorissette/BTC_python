from Block import Block
import hashlib

ledger=[{
  "timestamp": '1964-01-01',
  "description": "Second transaction",
  "payee": "I got my BTC",
  "payer": "I pay you BTC",
},{
  "timestamp": '1964-01-02',
  "description": "Third transaction",
  "payee": "I got my BTC",
  "payer": "I pay you BTC",
},{
  "timestamp": '1964-01-03',
  "description": "Fourth transaction",
  "payee": "I got my BTC",
  "payer": "I pay you BTC",
},]
genesis_block = Block("Chancellor is the house",{
  "timestamp": '1963-12-31',
  "description": "First transaction",
  "payee": "I got my BTC",
  "payer": "I pay you BTC",
})

def createBlockchain(root,ledger) :

  blockchain=[root]
  for transaction in ledger:
    root = Block(root.block_hash,transaction)
    blockchain.append(root)
  
  return blockchain

def printBlockchain(ledger) :
  i=0
  for node in ledger:
    if i==1:
      print('------------------------------')
    for x, y in node.transations.items():
      print("{:15}".format(x),":", y)
    print("{:15}".format("hash"),":",node.block_hash)
    if i == 1:
      print('------------------------------')
    i=i+1  

printBlockchain(createBlockchain(genesis_block,ledger))

#If the 2nd transation is change BTC to ETC
ledger.remove({
  "timestamp": '1964-01-01',
  "description": "Second transaction",
  "payee": "I got my BTC",
  "payer": "I pay you BTC",
})

ledger.insert(0,{
  "timestamp": '1964-01-01',
  "description": "Second transaction",
  "payee": "I got my <ETC>>>>>>>>>>>>>>>",
  "payer": "I pay you <ETC>>>>>>>>>>>>>>>",
})
print('')
print('+++++++++++++++++++++++++++++++++++++++++++')
print('||    If we change the 2nd transation     ||')
print('+++++++++++++++++++++++++++++++++++++++++++')
print('')
printBlockchain(createBlockchain(genesis_block,ledger))
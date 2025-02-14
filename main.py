from BlockChainProject.blockchain import Blockchain

# Krijo një blockchain të ri
my_blockchain = Blockchain(difficulty=4)

# Shto disa transaksione
my_blockchain.add_transaction({"from": "Alice", "to": "Bob", "amount": 10})
my_blockchain.add_transaction({"from": "Bob", "to": "Charlie", "amount": 5})

# Minimi i blloqeve
print("Mining block 1...")
my_blockchain.mine_pending_transactions()

my_blockchain.add_transaction({"from": "Charlie", "to": "David", "amount": 3})

print("Mining block 2...")
my_blockchain.mine_pending_transactions()

# Shfaq blockchain-in
my_blockchain.display_chain()

# Kontrollo nëse zinxhiri është i vlefshëm
print("Is blockchain valid?", my_blockchain.is_chain_valid())

# Blockchain Report

## Overview
This project implements a simple blockchain using Python. It includes:
- Block structure with hash-based security
- Proof of Work (PoW) mining
- Chain validation

## Code Explanation

### Block Class
Each block has:
- `index`: Position in the chain
- `previous_hash`: Links to the previous block
- `transactions`: Stores transaction data
- `timestamp`: Stores the creation time
- `nonce`: Used for Proof of Work
- `hash`: Ensures integrity

### Blockchain Class
- `create_genesis_block()`: Creates the first block
- `add_transaction()`: Adds pending transactions
- `mine_pending_transactions()`: Mines a new block
- `is_chain_valid()`: Checks the chain’s validity

## Consensus Mechanism
The system uses **Proof of Work (PoW)** where miners find a valid hash by incrementing a nonce. A block is valid only if its hash starts with a specific number of zeros.

## Security & Integrity
1. Each block links to the previous block using a hash.
2. Tampering with a block invalidates the entire chain.

## Usage Example
Run `python main.py` to add transactions, mine blocks, and verify the blockchain.

## Conclusion
This simple blockchain demonstrates core blockchain concepts, security through hashing, and consensus with Proof of Work.

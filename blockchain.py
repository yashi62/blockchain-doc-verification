import json
from web3 import Web3

class Blockchain:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))  # Replace with your Ethereum node address
        self.contract_address = 'YOUR_CONTRACT_ADDRESS'
        self.abi = json.load(open('contract/DocumentVerification_abi.json'))
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=self.abi)
        self.account = self.w3.eth.accounts[0]  # Use the first account for transactions

    def add_document(self, doc_hash):
        tx = self.contract.functions.addDocument(doc_hash).buildTransaction({
            'from': self.account,
            'nonce': self.w3.eth.getTransactionCount(self.account),
            'gas': 3000000,
            'gasPrice': self.w3.toWei('20', 'gwei')
        })
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key='YOUR_PRIVATE_KEY')
        tx_hash = self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return tx_hash.hex()

    def verify_document(self, doc_hash):
        return self.contract.functions.verifyDocument(doc_hash).call()

    def get_document_owner(self, doc_hash):
        return self.contract.functions.getDocumentOwner(doc_hash).call()

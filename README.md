# Blockchain Document Verification System

A Python-based blockchain system for document verification using Ethereum.

## Features
- Add document hashes to the blockchain.
- Verify document existence on the blockchain.
- Retrieve the owner of a document.

## Setup

### Prerequisites
- Python 3.8 or higher.
- Ethereum blockchain (local or testnet).
- Smart contract deployed.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/blockchain-document-verification.git
   cd blockchain-document-verification
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Replace placeholders in `blockchain.py`:
   - `YOUR_CONTRACT_ADDRESS`
   - `YOUR_PRIVATE_KEY`

4. Start the Flask server:
   ```bash
   python app.py
   ```

5. Use the API:
   - **Add Document**:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"doc_hash": "hash123"}' http://127.0.0.1:5000/add_document
     ```
   - **Verify Document**:
     ```bash
     curl -X GET "http://127.0.0.1:5000/verify_document?doc_hash=hash123"
     ```
   - **Get Document Owner**:
     ```bash
     curl -X GET "http://127.0.0.1:5000/get_document_owner?doc_hash=hash123"
     ```

## License
MIT

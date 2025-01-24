from flask import Flask, request, jsonify
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/add_document', methods=['POST'])
def add_document():
    data = request.json
    doc_hash = data.get('doc_hash')

    if not doc_hash:
        return jsonify({'error': 'Document hash is required'}), 400

    try:
        tx_hash = blockchain.add_document(doc_hash)
        return jsonify({'message': 'Document added successfully', 'transaction_hash': tx_hash}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/verify_document', methods=['GET'])
def verify_document():
    doc_hash = request.args.get('doc_hash')

    if not doc_hash:
        return jsonify({'error': 'Document hash is required'}), 400

    try:
        is_verified = blockchain.verify_document(doc_hash)
        return jsonify({'verified': is_verified}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_document_owner', methods=['GET'])
def get_document_owner():
    doc_hash = request.args.get('doc_hash')

    if not doc_hash:
        return jsonify({'error': 'Document hash is required'}), 400

    try:
        owner = blockchain.get_document_owner(doc_hash)
        return jsonify({'owner': owner}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

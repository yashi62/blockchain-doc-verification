// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DocumentVerification {
    mapping(string => address) private documentRegistry;

    event DocumentAdded(string indexed docHash, address indexed owner);

    function addDocument(string memory docHash) public {
        require(documentRegistry[docHash] == address(0), "Document already exists");
        documentRegistry[docHash] = msg.sender;
        emit DocumentAdded(docHash, msg.sender);
    }

    function verifyDocument(string memory docHash) public view returns (bool) {
        return documentRegistry[docHash] != address(0);
    }

    function getDocumentOwner(string memory docHash) public view returns (address) {
        require(documentRegistry[docHash] != address(0), "Document not found");
        return documentRegistry[docHash];
    }
}

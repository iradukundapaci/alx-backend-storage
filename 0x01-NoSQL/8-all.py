#!/usr/bin/env python3
"""
Script to list all documents in a collection
"""
from typing import List


def list_all(mongo_collection) -> List[object]:
    """
    Function that receives a mongo collection

    args:
        mongo_collection: collection name

    return: list of documents in collection
    """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents

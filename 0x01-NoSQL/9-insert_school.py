#!/usr/bin/env python3
"""
Script to insert documents in a collection
"""
from typing import List


def insert_school(mongo_collection, **kwargs):
    """
    Function that inserts given document into given colection

    args:
        mongo_collection: collection name
        **kwargs: document to insert

    return: document id
    """
    document_id = mongo_collection.insert_one(kwargs).inserted_id

    return document_id

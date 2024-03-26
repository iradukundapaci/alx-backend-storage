#!/usr/bin/env python3
"""
Script to update document topics
"""


def update_topics(mongo_collection, name, topics):
    """
    Function update document topics

    args:
        mongo_collection: collection name
        name: document name
        topics: list of topics

    return: None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

#!/usr/bin/env python3
"""
Script to filter school by topics
"""


def schools_by_topic(mongo_collection, topic):
    """
    Function filter school by topics

    args:
        mongo_collection: collection name
        topics: topic

    return: list of results
    """
    docs = mongo_collection.find({"topics": topic})

    return list(docs)

#!/usr/bin/env python3
"""this script to updatee doc in a collection"""


def update_topics(mongo_collection, name, topics):
    """update a doc into collection"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})

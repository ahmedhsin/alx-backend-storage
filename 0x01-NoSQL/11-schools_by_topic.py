#!/usr/bin/env python3
"""this script to find doc in a collection"""


def schools_by_topic(mongo_collection, topic):
    """find a doc into collection"""
    return mongo_collection.find({'topics': {'$in': [topic]}})

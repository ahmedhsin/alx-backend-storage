#!/usr/bin/env python3
"""this script to return all docs in a collection"""


def list_all(mongo_collection):
    """list all docs"""
    return mongo_collection.find()

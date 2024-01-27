#!/usr/bin/env python3
"""this script to insert doc in a collection"""


def insert_school(mongo_collection, **kwargs):
    """insert a doc into collection"""
    res = mongo_collection.insert_one(kwargs)
    return str(res.inserted_id)

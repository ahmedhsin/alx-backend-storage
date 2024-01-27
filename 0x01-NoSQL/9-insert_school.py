#!/usr/bin/env python3
"""this script to insert doc in a collection"""


def insert_school(mongo_collection, **kwargs):
    """insert a doc into collection"""
    try:
        res = mongo_collection.insert_one(kwargs)
        return res.inserted_id
    except Exception:
        pass

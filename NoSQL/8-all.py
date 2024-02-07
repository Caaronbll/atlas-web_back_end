#!/usr/bin/env python3
""" Task 8 """

import pymongo


def list_all(mongo_collection):
    """ lists all documents in a collection """

    if mongo_collection:
        return list(mongo_collection.find())
    return []

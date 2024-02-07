#!/usr/bin/env python3
""" Task 10 """
import pymongo


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school document based """

    return mongo_collection.update_many({ "name": name }, { "$set": { "topics": topics } })

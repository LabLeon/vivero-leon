#!/usr/bin/python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
# import pandas as pd

# Access to MongoDB remote cluster:
MONGO_URI = ""


def db_connect_to_collection(MONGO_URI, database, collection):
    """Function to connect to MongoDB data colletion."""

    # Connect to MongoClient:
    client = MongoClient(MONGO_URI)
    database = client[database]
    collection = database[collection]
    return collection


def db_fetch_data(collection, conditions={}):
    """Funciton to fetch data from collection."""

    # List all documents registered at date:
    cursor = collection.find(conditions)
    return cursor


def db_insert_document(collection, document):
    """Function to insert a new document in colletion."""

    return collection.insert_one(document)


# def db_fill_from_csv():
#     # Connect to DB:
#     print("[INFO] Connecting to database...")
#     donations = db_connect_to_collection(MONGO_URI, 'viveros', 'donaciones')
#
#     # Load Excel file:
#     print("[INFO] Reading CSV file...")
#     df = pd.read_csv('viveros.csv')
#     total = len(df)
#
#     # Fill database from Excel file:
#     for _, item in df.iterrows():
#         print("[INFO] * Inserting point %d from %d." % (_ + 1, total))
#         if item['Envase'] != (None or '' or ' '):
#             donation = {
#                 'fecha': item['Fecha'],
#                 'envase': item['Envase'],
#                 'piezas': item['Piezas'],
#                 'especie': item['Especie']
#             }
#             db_insert_document(donations, donation)
#     print("[INFO] Insertion finished.")
#     return


if __name__ == '__main__':
    # This section was used to fill the database.
    # It will stay commented since it has been done already.
    # db_fill_from_csv()
    pass

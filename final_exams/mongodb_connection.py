"""
---------------------
Creates a connection to the MongoDB database.

Database:
    Amazon_EN_Reviews

Collections:
    ReviewData
    ProductData
"""

from pymongo import MongoClient


def connect_db():
    """
    Connect to the local MongoDB server and
    return the Amazon_EN_Reviews database.
    """

    try:
        # Connect to MongoDB Compass / MongoDB Community Server
        client = MongoClient("mongodb://localhost:27017/")

        # Test the connection
        client.admin.command("ping")

        print("\n[OK] Connected to MongoDB")

        # Return the database
        db = client["Amazon_EN_Reviews"]

        return db

    except Exception as error:

        print("\n[ERROR] Could not connect to MongoDB.")
        print(error)

        return None
```

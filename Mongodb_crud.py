"""
mongodb_crud.py
=============================
CRUD operations for MongoDB (Week 2)
Dataset: sample_repos.json
Schema: repo_name, watch_count
"""

import json
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


# -----------------------------------------------------
# CONNECTION
# -----------------------------------------------------

def connect_to_mongodb(
    uri="mongodb://localhost:27017/",
    database="GitHubArchive_Mongo",
    collection="Repos"
):

    try:
        client = MongoClient(uri)
        client.admin.command("ping")

        print("[OK] Connected to MongoDB")

        db = client[database]
        return db[collection]

    except ConnectionFailure:
        print("[ERROR] MongoDB connection failed")
        return None


# -----------------------------------------------------
# LOAD DATA (sample_repos.json)
# -----------------------------------------------------

def load_github_data(filepath):

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        print(f"[OK] Loaded {len(data)} repositories")
        return data

    except Exception as e:
        print("[ERROR]", e)
        return []


# -----------------------------------------------------
# CREATE
# -----------------------------------------------------

def bulk_create_commits(collection, data):

    if not collection or not data:
        return

    collection.delete_many({})
    collection.insert_many(data)

    print(f"[OK] Inserted {len(data)} records")


# -----------------------------------------------------
# READ
# -----------------------------------------------------

def read_commit(collection, repo_name):

    return collection.find_one({"repo_name": repo_name})


# -----------------------------------------------------
# UPDATE
# -----------------------------------------------------

def update_commit(collection, repo_name, updates):

    result = collection.update_one(
        {"repo_name": repo_name},
        {"$set": updates}
    )

    print("[OK] Updated" if result.modified_count else "[WARN] Not found")


# -----------------------------------------------------
# DELETE
# -----------------------------------------------------

def delete_commit(collection, repo_name):

    result = collection.delete_one({"repo_name": repo_name})

    print("[OK] Deleted" if result.deleted_count else "[WARN] Not found")


# -----------------------------------------------------
# LIST IDS
# -----------------------------------------------------

def list_all_commit_ids(collection, limit=20):

    cursor = collection.find({}, {"repo_name": 1, "_id": 0}).limit(limit)

    return [doc["repo_name"] for doc in cursor]

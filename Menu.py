"""
menu.py — GitHub Multi-Database System
======================================
Redis (Week 1) + MongoDB (Week 2)
"""

import json

import redis_crud
import redis_features

import mongodb_crud
import mongodb_features


# =====================================================
# REDIS FUNCTIONS 
# =====================================================

def display_top_repos(client, top_n=10):

    repos = redis_features.get_top_repos(client, top_n)

    print("\nTop Repositories:")

    for i, (repo, count) in enumerate(repos, 1):
        print(f"{i}. {repo} ({count})")


def display_keyword_analysis(client):

    data = redis_features.get_commit_keyword_frequencies(client, 15)

    total = sum(c for _, c in data)

    for word, count in data:
        pct = (count / total) * 100 if total else 0
        print(f"{word}: {pct:.1f}%")


def display_top_contributors(client, top_n=10):

    data = redis_features.get_top_contributors(client, top_n)

    for i, (author, count) in enumerate(data, 1):
        print(f"{i}. {author} ({count})")


def display_author_history(client, author):

    data = redis_features.get_author_contribution_history(client, author)

    print(data["author_name"])
    print(data["total_commits"])


# =====================================================
# REDIS MENU
# =====================================================

def run_redis_menu(data_filepath="Project/data/Commits.json"):

    client = redis_crud.connect_to_redis()

    while True:

        print("\n--- REDIS MENU ---")
        print("1 Load")
        print("2 Read")
        print("3 Update")
        print("4 Delete")
        print("5 List SHAs")
        print("6 Top Repos")
        print("7 Keywords")
        print("8 Contributors")
        print("9 Author History")
        print("0 Back")

        choice = input("Choice: ")

        if choice == "1":

            commits = redis_crud.load_github_data(data_filepath)

            redis_crud.bulk_create_commits(client, commits)

            redis_features.build_repo_activity_index(client, commits)
            redis_features.build_commit_keyword_index(client, commits)
            redis_features.build_author_contribution_index(client, commits)

            print("[OK] Loaded Redis data")

        elif choice == "2":

            sha = input("SHA: ")
            print(redis_crud.read_commit(client, sha))

        elif choice == "3":

            sha = input("SHA: ")
            field = input("Field: ")
            value = input("Value: ")

            redis_crud.update_commit(client, sha, {field: value})

        elif choice == "4":

            sha = input("SHA: ")
            redis_crud.delete_commit(client, sha)

        elif choice == "5":

            print(redis_crud.list_all_commit_ids(client))

        elif choice == "6":

            display_top_repos(client)

        elif choice == "7":

            display_keyword_analysis(client)

        elif choice == "8":

            display_top_contributors(client)

        elif choice == "9":

            author = input("Author: ")
            display_author_history(client, author)

        elif choice == "0":
            break


# =====================================================
# MONGODB MENU 
# =====================================================

def run_mongodb_menu(data_filepath="Project/data/sample_repos.json"):

    collection = mongodb_crud.connect_to_mongodb()

    while True:

        print("\n--- MONGODB MENU ---")
        print("1 Load")
        print("2 Read")
        print("3 Update")
        print("4 Delete")
        print("5 List Repos")
        print("6 Repo Lengths")
        print("7 Top Watch Count")
        print("8 Watch Analysis")
        print("0 Back")

        choice = input("Choice: ")

        if choice == "1":

            data = mongodb_crud.load_github_data(data_filepath)

            mongodb_crud.bulk_create_commits(collection, data)

        elif choice == "2":

            name = input("Repo name: ")
            print(mongodb_crud.read_commit(collection, name))

        elif choice == "3":

            name = input("Repo name: ")
            field = input("Field: ")
            value = input("Value: ")

            mongodb_crud.update_commit(collection, name, {field: value})

        elif choice == "4":

            name = input("Repo name: ")
            mongodb_crud.delete_commit(collection, name)

        elif choice == "5":

            print(mongodb_crud.list_all_commit_ids(collection))

        elif choice == "6":

            mongodb_features.display_repo_name_lengths(collection)

        elif choice == "7":

            mongodb_features.display_repository_distribution(collection)

        elif choice == "8":

            mongodb_features.display_common_commit_words(collection)

        elif choice == "0":
            break


# =====================================================
# MAIN MENU
# =====================================================

def run_app():

    while True:

        print("\n=== MAIN MENU ===")
        print("1 Redis")
        print("2 MongoDB")
        print("0 Exit")

        choice = input("Choice: ")

        if choice == "1":
            run_redis_menu()

        elif choice == "2":
            run_mongodb_menu()

        elif choice == "0":
            break


if __name__ == "__main__":
    run_app()

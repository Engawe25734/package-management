"""
mongodb_features.py
=============================
MongoDB analytics features (Week 2)
Dataset: sample_repos.json
Schema: repo_name, watch_count
"""

# -----------------------------------------------------
# FEATURE 1: REPO NAME LENGTH ANALYSIS
# -----------------------------------------------------

def display_repo_name_lengths(collection):

    if not collection:
        return

    repos = list(collection.find({}, {"repo_name": 1, "_id": 0}))
    names = [r.get("repo_name", "") for r in repos]

    if not names:
        print("No data found")
        return

    longest = max(names, key=len)
    shortest = min(names, key=len)

    print("\n=== Repository Name Analysis ===")
    print(f"Longest: {longest}")
    print(f"Shortest: {shortest}")


# -----------------------------------------------------
# FEATURE 2: TOP WATCHED REPOSITORIES
# -----------------------------------------------------

def display_repository_distribution(collection):

    if not collection:
        return

    pipeline = [
        {"$sort": {"watch_count": -1}},
        {"$limit": 10}
    ]

    results = list(collection.aggregate(pipeline))

    print("\n=== Top Repositories by Watch Count ===")

    for i, r in enumerate(results, 1):

        repo = r.get("repo_name", "Unknown")
        watch = r.get("watch_count", 0)

        bar = "█" * min(watch // 5, 30)

        print(f"{i}. {repo:<35} {watch:<6} {bar}")


# -----------------------------------------------------
# FEATURE 3: WATCH STATISTICS
# -----------------------------------------------------

def display_common_commit_words(collection):

    if not collection:
        return

    repos = list(collection.find({}, {"watch_count": 1}))

    values = [r.get("watch_count", 0) for r in repos]

    if not values:
        print("No data found")
        return

    avg = sum(values) / len(values)

    above = sum(1 for v in values if v > avg)
    below = len(values) - above

    print("\n=== Watch Count Analysis ===")
    print(f"Average watch count: {avg:.2f}")
    print(f"Above average: {above}")
    print(f"Below average: {below}")


# -----------------------------------------------------
# OPTIONAL
# -----------------------------------------------------

def get_total_repos(collection):

    return collection.count_documents({})

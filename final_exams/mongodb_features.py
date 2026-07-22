"""
MongoDB search and analysis features.

Uses:
    distinct()
    count_documents()
    $regex
"""



# ============================================================
# DISPLAY ALL DISTINCT PRODUCT CATEGORIES
# ============================================================

def display_categories(db):

    collection = db["ProductData"]


    categories = collection.distinct(
        "product_category"
    )


    print("\nProduct Categories")
    print("-------------------")


    for category in categories:

        print(category)





# ============================================================
# COUNT 4 AND 5 STAR REVIEWS
# ============================================================

def count_good_reviews(db):

    category = input(
        "Enter product category: "
    )


    collection = db["ReviewData"]


    count = collection.count_documents(

        {

            "product_category": category,

            "stars":
                {
                    "$in":
                    [
                        4,
                        5
                    ]
                }

        }

    )


    print(
        "\n4-5 Star Reviews:",
        count
    )





# ============================================================
# COUNT 1 AND 2 STAR REVIEWS
# ============================================================

def count_bad_reviews(db):

    category = input(
        "Enter product category: "
    )


    collection = db["ReviewData"]


    count = collection.count_documents(

        {

            "product_category": category,


            "stars":
                {
                    "$in":
                    [
                        1,
                        2
                    ]
                }

        }

    )


    print(
        "\n1-2 Star Reviews:",
        count
    )





# ============================================================
# SEARCH REVIEW TITLE USING REGEX
# ============================================================

def search_title(db):

    word = input(
        "Enter word in review title: "
    )


    collection = db["ReviewData"]


    results = collection.find(

        {

            "review_title":
                {

                    "$regex":
                        word,

                    "$options":
                        "i"

                }

        }

    )


    print("\nMatching Titles")
    print("----------------")


    found = False


    for review in results:

        found = True

        print(
            review.get("review_title")
        )


    if not found:

        print(
            "No reviews found."
        )





# ============================================================
# SEARCH REVIEW BODY USING REGEX
# ============================================================

def search_body(db):

    word = input(
        "Enter word in review body: "
    )


    collection = db["ReviewData"]


    results = collection.find(

        {

            "review_body":
                {

                    "$regex":
                        word,

                    "$options":
                        "i"

                }

        }

    )


    print("\nMatching Reviews")
    print("----------------")


    found = False


    for review in results:


        found = True


        print(
            review.get("review_body")
        )



    if not found:

        print(
            "No reviews found."
        )
```

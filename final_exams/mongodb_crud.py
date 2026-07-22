"""
MongoDB CRUD operations for Amazon EN Reviews.

Collections:
    ReviewData
    ProductData
"""

import json



# ============================================================
# LOAD JSON DATA INTO MONGODB
# ============================================================

def load_json_data(db):

    filename = "dataset_en_dev.json"

    try:

        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)


        review_collection = db["ReviewData"]
        product_collection = db["ProductData"]


        reviews = []
        products = []


        for item in data:


            # Convert stars from string to integer
            stars = int(item.get("stars", 0))


            # ReviewData document
            review = {

                "review_id": item.get("review_id"),

                "product_id": item.get("product_id"),

                "reviewer_id": item.get("reviewer_id"),

                "stars": stars,

                "review_title": item.get("review_title"),

                "review_body": item.get("review_body"),

                "language": item.get("language"),

                "product_category": item.get("product_category")

            }


            reviews.append(review)



            # ProductData document
            product = {

                "product_id": item.get("product_id"),

                "product_category":
                    item.get("product_category")

            }


            products.append(product)



        if reviews:

            review_collection.insert_many(
                reviews
            )


        if products:

            product_collection.insert_many(
                products
            )


        print("\n================================")
        print("[OK] JSON IMPORT COMPLETE")
        print("================================")
        print("Reviews loaded:", len(reviews))
        print("Products loaded:", len(products))


    except FileNotFoundError:

        print("\n[ERROR] dataset_en_dev.json not found")


    except Exception as error:

        print("\n[ERROR]", error)
# ============================================================
# INSERT NEW REVIEW
# ============================================================

def insert_review(db):

    collection = db["ReviewData"]


    review = {

        "review_id":
            input("Review ID: "),


        "product_id":
            input("Product ID: "),


        "reviewer_id":
            input("Reviewer ID: "),


        "stars":
            int(input("Stars: ")),


        "review_title":
            input("Review Title: "),


        "review_body":
            input("Review Body: ")

    }


    collection.insert_one(review)


    print("\n[OK] Review inserted.")





# ============================================================
# INSERT NEW PRODUCT
# ============================================================

def insert_product(db):

    collection = db["ProductData"]


    product = {


        "product_id":
            input("Product ID: "),


        "product_category":
            input("Category: "),


        "product_name":
            input("Product Name: ")

    }


    collection.insert_one(product)


    print("\n[OK] Product inserted.")





# ============================================================
# FIND REVIEW BY REVIEW ID
# ============================================================

def find_review(db):

    collection = db["ReviewData"]


    review_id = input(
        "Enter review ID: "
    )


    result = collection.find_one(
        {
            "review_id": review_id
        }
    )


    if result:

        print("\nReview Found")
        print("----------------")

        for key, value in result.items():

            print(
                key,
                ":",
                value
            )


    else:

        print("\nReview not found.")





# ============================================================
# DELETE REVIEW
# ============================================================

def delete_review(db):

    collection = db["ReviewData"]


    review_id = input(
        "Enter review ID to delete: "
    )


    result = collection.delete_one(
        {
            "review_id": review_id
        }
    )


    if result.deleted_count:

        print("\n[OK] Review deleted.")

    else:

        print("\nReview not found.")





# ============================================================
# DELETE COLLECTIONS
# ============================================================

def delete_collections(db):


    answer = input(
        "Delete ReviewData and ProductData? (Y/N): "
    )


    if answer.lower() == "y":


        db["ReviewData"].drop()

        db["ProductData"].drop()


        print(
            "\n[OK] Collections deleted."
        )


    else:

        print(
            "\nDelete cancelled."
        )
```

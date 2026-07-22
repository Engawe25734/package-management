```python
"""
Name: Elvis Ngawe
Date: July 22, 2026
Course: SDC435
Final Exam - Option 1 (MongoDB)

Program Summary:
This program manages Amazon English Review data using MongoDB.
It allows the user to load JSON data, insert and delete records,
search reviews, display product categories, and perform review
statistics using a menu-driven interface.
"""

from mongodb_connection import connect_db
from mongodb_crud import (
    load_json_data,
    insert_review,
    insert_product,
    find_review,
    delete_review,
    delete_collections
)

from mongodb_features import (
    display_categories,
    count_good_reviews,
    count_bad_reviews,
    search_title,
    search_body
)


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 55)
    print("      Amazon EN Reviews - MongoDB")
    print("=" * 55)
    print("1. Load JSON Data")
    print("2. Insert Review")
    print("3. Insert Product")
    print("4. Find Review by Review ID")
    print("5. Display Product Categories")
    print("6. Count 4-5 Star Reviews by Category")
    print("7. Count 1-2 Star Reviews by Category")
    print("8. Search Review Titles ($regex)")
    print("9. Search Review Bodies ($regex)")
    print("10. Delete Review")
    print("11. Delete ReviewData and ProductData")
    print("0. Exit")
    print("=" * 55)


def main():

    db = connect_db()

    if db is None:
        return

    while True:

        display_menu()

        choice = input("Enter choice: ")

        if choice == "1":
            load_json_data(db)

        elif choice == "2":
            insert_review(db)

        elif choice == "3":
            insert_product(db)

        elif choice == "4":
            find_review(db)

        elif choice == "5":
            display_categories(db)

        elif choice == "6":
            count_good_reviews(db)

        elif choice == "7":
            count_bad_reviews(db)

        elif choice == "8":
            search_title(db)

        elif choice == "9":
            search_body(db)

        elif choice == "10":
            delete_review(db)

        elif choice == "11":
            delete_collections(db)

        elif choice == "0":
            print("\nThank you for using the program.")
            break

        else:
            print("\nInvalid menu option.")


if __name__ == "__main__":
    main()
```

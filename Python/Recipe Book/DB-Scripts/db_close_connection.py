import sqlite3

def get_db_connection():
    return sqlite3.connect(r"S:\Python\Recipe Book\Data\recipe_database.db")

def main():
    print("Starting the script...")

    # Create a database connection
    connection = get_db_connection()

    try:
        # Perform database operations (e.g., querying, inserting, updating)
        # ...

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the connection
        connection.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()
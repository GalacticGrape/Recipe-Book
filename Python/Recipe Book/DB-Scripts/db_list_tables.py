import sqlite3

def list_tables(database_path):
    try:
        # Connect to the database
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        # Query to retrieve table names
        query = "SELECT name FROM sqlite_master WHERE type='table';"

        # Execute the query
        cursor.execute(query)

        # Fetch all table names
        tables = cursor.fetchall()

        # Close the cursor and the connection
        cursor.close()
        connection.close()

        return [table[0] for table in tables]

    except sqlite3.Error as e:
        print("SQLite error:", e)
        return None

# Example usage
database_path = r"S:\Python\Recipe Book\Data\recipe_database.db"
tables = list_tables(database_path)

if tables:
    print("Tables in the database:")
    for table in tables:
        print("- " + table)
else:
    print("Failed to retrieve table names.")
    
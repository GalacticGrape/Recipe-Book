import sqlite3

def create_categories_table():
    try:
        # Connect to the database. If it doesn't exist, it will be created.
        connection = sqlite3.connect(r"S:\Python\Recipe Book\Data\recipe_database.db")
        
        # Create a cursor
        cursor = connection.cursor()
        
        # Define the table creation SQL query for categories
        create_table_query = """
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        """
        
        # Execute the table creation query for categories
        cursor.execute(create_table_query)
        
        # Commit and close the connection
        connection.commit()
        print("Categories table created successfully!")
        
    except sqlite3.Error as e:
        print("SQLite error:", e)
        
    finally:
        # Close the connection
        connection.close()
        print("Changes committed and db connection closed")

# Call the function to create the "categories" table
create_categories_table()
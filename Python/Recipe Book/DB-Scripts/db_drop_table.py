import sqlite3

def drop_table(table_name):
    try:
        # Connect to the database
        connection = sqlite3.connect(r"S:\Python\Recipe Book\Data\recipe_database.db")
        
        # Create a cursor
        cursor = connection.cursor()
        
        # Drop the specified table
        drop_query = f"DROP TABLE IF EXISTS {table_name};"
        cursor.execute(drop_query)
        
        # Commit the change and close the connection
        connection.commit()
        print(f"Table '{table_name}' dropped successfully!")
        
    except sqlite3.Error as e:
        print("SQLite error:", e)
        
    finally:
        # Close the connection
        connection.close()
        print("Changes committed and db connection closed")

# Call the function to drop the 'categories' table
drop_table('categories')
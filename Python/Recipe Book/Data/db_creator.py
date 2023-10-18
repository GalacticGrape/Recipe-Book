import sqlite3

def get_db_connection():
    # Connect to the database. If it doesn't exist, it will be created.
    connection = sqlite3.connect(r"S:\Python\Recipe Book\Data\recipe_database.db")
    return connection

def create_table():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Define the table creation SQL query
    create_table_query = """
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        ingredients TEXT NOT NULL,
        instructions TEXT NOT NULL
    );
    """

    # Execute the table creation query
    cursor.execute(create_table_query)

    # Commit and close the connection
    connection.commit()
    connection.close()

# Call the function to create the table (call this function once at the start of your application)
create_table()

# Now you can use the get_db_connection() function to connect to the database for other operations.

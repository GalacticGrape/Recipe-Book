import mysql.connector
import os
from dotenv import load_dotenv

# Specify the path to the .env file
dotenv_path = r"S:\Python\.env"

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

try:
    # Create a connection to the database
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    # Create a cursor object using the connection
    cursor = connection.cursor()

    # Now you can execute SQL queries using the cursor
    # For example, creating tables
    create_table_query = """
    CREATE TABLE IF NOT EXISTS recipe_categories (
        category_name VARCHAR(255) PRIMARY KEY
    );

    CREATE TABLE IF NOT EXISTS recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        ingredients TEXT,
        instructions TEXT,
        category_name VARCHAR(255),
        FOREIGN KEY (category_name) REFERENCES recipe_categories(category_name)
    );
    """

    cursor.execute(create_table_query)

    # Commit the changes
    connection.commit()

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    # Close the connection in the 'finally' block to ensure it's always closed
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
# This Python script establishes a connection to a MySQL database using the specified environment variables for host, user, password, and database name, sourced from a .env file to create two tables 

# Import necessary modules and environment variables
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

# Within a try block, the script initiates a connection to the MySQL server
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
    
    # The script creates a table named recipe_categories with a single column category_name of type VARCHAR(255)
    # This table is intended to store various categories of recipes, making category_name the primary key
    # Create recipe_categories table
    create_categories_table_query = """
    CREATE TABLE IF NOT EXISTS recipe_categories (
        category_name VARCHAR(255) PRIMARY KEY
    );
    """
    cursor.execute(create_categories_table_query)

    # Another table named recipes is created
    # This table includes columns for id (an auto-incremented primary key), name (for recipe names), instructions (for recipe instructions), and category_name (for the category of the recipe).
    # The category_name column is set as a foreign key, referencing the category_name column in the recipe_categories table
    # Create recipes table
    create_recipes_table_query = """
    CREATE TABLE IF NOT EXISTS recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        instructions TEXT,
        category_name VARCHAR(255),
        FOREIGN KEY (category_name) REFERENCES recipe_categories(category_name)
    );
    """
    cursor.execute(create_recipes_table_query)
    # After creating the tables, the script commits the changes to the database to make the changes permanent

    # Commit the changes
    connection.commit()

# In case of any errors during the database operations, the script prints an error message 
except mysql.connector.Error as error:
    print("Error:", error)

# The finally block ensures the connection is closed properly, regardless of whether the operations were successful or not
finally:
    # Close the connection in the 'finally' block to ensure it's always closed
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
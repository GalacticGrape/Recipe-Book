# This Python module establishes a connection to and queries the recipes database to list off recipe_categories

# This line imports the mysql.connector module, which is a Python driver for MySQL databases
# A module in Python is a file containing Python definitions and statements
# By importing mysql.connector, you gain access to functions and classes that allow you to interact with MySQL databases in your Python script
import mysql.connector

# The os module provides a way of interacting with the operating system, it is used for working with file paths
# It's used to locate and load the .env file that contains environment variables
import os

# The dotenv module is used for reading variables from a .env file into the environment
# 'load_dotenv' is a function provided by this module that loads environment variables from a .env file into the script's environment
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
# Within a try block, the script initiates a connection to the MySQL server:
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

    # Check if recipe_categories table exists
    check_categories_table_query = """
    SHOW TABLES LIKE 'recipe_categories';
    """
    cursor.execute(check_categories_table_query)

    # Fetch all rows from the query result
    tables = cursor.fetchall()

    # If recipe_categories table exists, fetch all categories
    if tables:
        # Query to select all categories from recipe_categories table
        select_categories_query = """
        SELECT category_name FROM recipe_categories;
        """
        cursor.execute(select_categories_query)
        
        # Fetch all rows from the query result
        categories = cursor.fetchall()

        # Print the categories
        print("Categories in recipe_categories table:")
        for category in categories:
            print(category[0])
    else:
        print("recipe_categories table does not exist.")

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    # Close the connection in the 'finally' block to ensure it's always closed
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
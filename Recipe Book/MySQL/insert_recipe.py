# This script is a test for inserting recipes into the database and will likely evolve into the main template

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

    # Insert a test recipe into the recipes table
    insert_recipe_query = """
    INSERT INTO recipes (name, instructions, category_name)
    VALUES (%s, %s, %s)
    """

    # Define the recipe details (name, instructions, and category_name)
    recipe_name = "Test Recipe"
    recipe_instructions = "Test instructions for baking the recipe."
    category_name = "Baked_Goods"  # Corrected category name

    # Data for the recipe
    recipe_data = (recipe_name, recipe_instructions, category_name)

    # Execute the insert query with the recipe data
    cursor.execute(insert_recipe_query, recipe_data)

    # Commit the changes to the database
    connection.commit()

# In case of any errors during the database operations, the script prints an error message.
except mysql.connector.Error as error:
    print("Error:", error)

# The finally block ensures the connection is closed properly, regardless of whether the operations were successful or not.
finally:
    # Close the connection in the 'finally' block to ensure it's always closed
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
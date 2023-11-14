# utils.py

import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector.connection import MySQLConnection
from typing import List

def import_dependencies():
    """
    Import necessary modules and retrieve environment variables.

    Returns:
    dict: A dictionary containing imported modules and environment variables.
    """
    dotenv_path = r"S:\Python\.env"
    load_dotenv()

    os_module = os
    dotenv_module = load_dotenv
    mysql_module = mysql.connector

    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")

    modules = {
        "os": os_module,
        "dotenv": dotenv_module,
        "mysql": mysql_module,
    }

    environment_vars = {
        "dotenv_path": dotenv_path,
        "db_host": db_host,
        "db_user": db_user,
        "db_password": db_password,
        "db_name": db_name
    }

    return modules, environment_vars


def get_categories(connection: MySQLConnection) -> List[str]:
    """
    Get available recipe categories from the database.

    Args:
    connection (mysql.connector.connection.MySQLConnection): Database connection object.

    Returns:
    list: List of available recipe categories.
    """
    categories = []
    try:
        cursor = connection.cursor()
        # Execute SQL query to retrieve categories from the database
        cursor.execute("SELECT category_name FROM recipe_categories")
        categories = [category[0] for category in cursor.fetchall()]
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
    return categories


def insert_recipe(recipe_name, instructions, category_name, connection):
    # global db_host, db_user, db_password, db_name  
        # Declare variables as global
        # commented out to troubleshoot

    """
    Insert a recipe into the database.

    Args:
    mysql (module): The mysql module for database connection.
    recipe_name (str): The name of the recipe.
    instructions (str): Instructions for the recipe.
    category_name (str): The category of the recipe.

    Returns:
    bool: True if insertion is successful, False otherwise.
    """
        # In this section, you define the insert_recipe function
        # This function takes three arguments: recipe_name, instructions, and category_name
        # Inside this function, you will write the code to insert these values into the database

    try:
            # Create a connection to the database
                
                # Create a cursor object using the connection
        with connection.cursor() as cursor:
            # Insert query
            insert_recipe_query = """
                INSERT INTO recipes (name, instructions, category_name)
                VALUES (%s, %s, %s)
                """

                # Data for the recipe
            recipe_data = (recipe_name, instructions, category_name)

                # Execute the insert query with the recipe data
            cursor.execute(insert_recipe_query, recipe_data)

                # Commit the changes to the database
            connection.commit()

        return True
            # Inside the try block, a connection to the database is established using the retrieved environment variables (db_host, db_user, db_password, db_name)
            # The recipe details provided as arguments are inserted into the recipes table using an SQL INSERT INTO query
            # The commit method is called to make the changes permanent in the database. If the insertion is successful, the function returns True


    except mysql.connector.Error as error:
        print("Error:", error)
        return False
        # In case there is an error during the database operations, the code inside the except block will execute
        # It prints the error message and returns False to indicate that the insertion failed


    finally:
        # Close the connection in the 'finally' block to ensure it's always closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")
        # The finally block ensures that the database connection is closed properly, regardless of whether the operations were successful or not
        # It checks if the connection is still open, and if so, it closes both the cursor and the connection

def query_by_category(category_name, connection):
    """
    Query the database by category.

    Args:
    category_name (str): The category to query.
    connection (mysql.connector.connection.MySQLConnection): Database connection object.

    Returns:
    List: List of recipes in the specified category.
    """
    recipes = []
    try:
        with connection.cursor() as cursor:
            # Execute SQL query to retrieve recipes from the specified category
            cursor.execute("SELECT name FROM recipes WHERE category_name = %s", (category_name,))
            recipes = [recipe[0] for recipe in cursor.fetchall()]

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        # Close the connection in the 'finally' block to ensure it's always closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

    return recipes


def query_by_recipe_name(recipe_name, connection):
    """
    Query the database by recipe name.

    Args:
    recipe_name (str): The recipe name to search for.
    connection (mysql.connector.connection.MySQLConnection): Database connection object.

    Returns:
    List: List of recipes with the specified name.
    """
    recipes = []
    try:
        cursor = connection.cursor()
        # Execute SQL query to retrieve recipes by name from the database
        query = "SELECT * FROM recipes WHERE name LIKE %s"
        cursor.execute(query, (f"%{recipe_name}%",))
        recipes = [{"name": row[1], "instructions": row[2], "category_name": row[3]} for row in cursor.fetchall()]
    except mysql.connector.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
    return recipes

# This new function displays a list of recipes
def display_recipe_list(recipes):
    print("Available recipes:")
    for index, recipe in enumerate(recipes, start=1):
        print(f"{index}. {recipe['name']}")
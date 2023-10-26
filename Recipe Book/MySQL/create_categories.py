# This script is for creating categories in the recipes_category table
# Please note - the category names will be used in the recipe table

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

def insert_category(category_name):
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

        # Insert category into recipe_categories table
        insert_category_query = """
        INSERT INTO recipe_categories (category_name)
        VALUES (%s)
        """
        category_data = (category_name,)
        cursor.execute(insert_category_query, category_data)

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

# Example usage - Inserting "Drinks" category into recipe_categories table
categories_to_insert = ["Drinks"]

# Capable of adding multiple categories 
# Example usage 
# categories_to_insert = ["Baked_Boods", "Canned_Goods", "Breakfast", "Lunch", "Dinner", "Jams_Jellys_Preserves", "Dried_goods", "Desserts", "Snacks", "EZ-PZ_Mealz"]

for category in categories_to_insert:
    insert_category(category)
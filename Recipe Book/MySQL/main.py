# main.py

from utils import import_dependencies, connection, insert_recipe_flow, get_categories, query_by_category_flow, query_by_recipe_name_flow
import mysql.connector

# Import dependencies and retrieve values
modules, db_vars = import_dependencies()

# Access individual variables from db_vars
db_host = db_vars["db_host"]
db_user = db_vars["db_user"]
db_password = db_vars["db_password"]
db_name = db_vars["db_name"]
 
# Access the mysql module from the modules dictionary
mysql_module = modules["mysql"]

# Access load_dotenv function from modules
load_dotenv = modules["dotenv"]

# Access dotenv_path variable from db_vars
dotenv_path = db_vars["dotenv_path"]

# Create a new connection
connection_obj = connection(db_host, db_user, db_password, db_name)

# Get categories
categories = get_categories(connection_obj)

def main():
    # Load environment variables from .env file
    load_dotenv(dotenv_path)

    # Get user choice
    choice = input("Choose an action (1: Insert Recipe, 2: Query by Category, 3: Query by Recipe Name): ")

    if choice == '1':
        # Insert a recipe into the database
        insert_recipe_flow(connection_obj)
    elif choice == '2':
        # Query the database by category
        query_by_category_flow(connection_obj, categories)
    elif choice == '3':
        # Query the database by recipe name
        query_by_recipe_name_flow(connection_obj)
    else:
        print("Invalid choice. Please choose a valid option.")

    # close connection when done
    connection_obj.close()

if __name__ == "__main__":
    main()

# main.py

from utils import import_dependencies, get_categories, insert_recipe, query_by_category, query_by_recipe_name, insert_recipe_flow, query_by_category_flow, display_recipe_list
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

# Get available categories
connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

def main():
    # Load environment variables from .env file
    load_dotenv(dotenv_path)

    # Get user choice
    choice = input("Choose an action (1: Insert Recipe, 2: Query by Category, 3: Query by Recipe Name): ")

    if choice == '1':
        # Insert a recipe into the database
        insert_recipe_flow(connection)
    elif choice == '2':
        # Query the database by category
        query_by_category_flow(connection)
    elif choice == '3':
        # Query the database by recipe name
        query_by_recipe_name_flow(connection)
    else:
        print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

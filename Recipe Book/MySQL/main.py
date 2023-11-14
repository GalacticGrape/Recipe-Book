# main.py

from utils import import_dependencies, get_categories, insert_recipe, query_by_category, query_by_recipe_name
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

def main():
    # Load environment variables from .env file
    load_dotenv(dotenv_path)

    # Get user choice
    choice = input("Choose an action (1: Insert Recipe, 2: Query by Category, 3: Query by Recipe Name): ")

    if choice == '1':
        # Insert a recipe into the database
        insert_recipe_flow()
    elif choice == '2':
        # Query the database by category
        query_by_category_flow()
    elif choice == '3':
        # Query the database by recipe name
        query_by_recipe_name_flow()
    else:
        print("Invalid choice. Please choose a valid option.")

def insert_recipe_flow():
    # Get recipe details from user input
    recipe_name = input("Enter recipe name: ")
    instructions = input("Enter recipe instructions: ")
    
    # Get available categories
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    categories = get_categories(connection)
    
    # Prompt user for category choice
    print("Available categories:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    # Get user choice for category
    category_choice = int(input("Choose a category: ")) - 1
    selected_category = categories[category_choice]
    
    # Insert the recipe into the database
    if insert_recipe(recipe_name, instructions, selected_category, connection):
        print("Recipe inserted successfully!")
    else:
        print("Failed to insert recipe.")

def query_by_category_flow():
    # Get available categories
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    categories = get_categories(connection)
    
    # Prompt user for category choice
    print("Available categories:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    # Get user choice for category
    category_choice = int(input("Choose a category: ")) - 1
    selected_category = categories[category_choice]

    # Query the database by category
    recipes = query_by_category(selected_category, connection)
    
    # Display the results
    if recipes:
        print(f"Recipes in the category '{selected_category}':")
        for recipe in recipes:
            print(recipe)
    else:
        print(f"No recipes found in the category '{selected_category}'.")

def display_recipe_list(recipes):
    print("Available recipes:")
    for index, recipe in enumerate(recipes, start=1):
        print(f"{index}. {recipe['name']}")

def query_by_recipe_name_flow():

    # Get user input for recipe name
    recipe_name = input("Enter a partial or full recipe name to search for: ")
    
    # Get available categories
    connection = mysql.connector.connect(
    
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    # Query the database by recipe name
    recipes = query_by_recipe_name(recipe_name, connection)

    # Display the results
    if recipes:
        display_recipe_list(recipes)
        recipe_choice = int(input("Choose a recipe: ")) - 1

        if 0 <= recipe_choice < len(recipes):
            selected_recipe = recipes[recipe_choice]
            print(f"Details for the selected recipe '{selected_recipe['name']}':")
            print(f"Instructions: {selected_recipe['instructions']}")
            print(f"Category: {selected_recipe['category_name']}")
        else:
            print("Invalid recipe choice.")
    else:
        print(f"No recipes found with the name '{recipe_name}'.")

if __name__ == "__main__":
    main()

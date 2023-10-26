# main.py

from utils import import_dependencies, get_categories, insert_recipe

# Import necessary modules and retrieve environment variables
dependencies = import_dependencies()
os = dependencies["os"]
load_dotenv = dependencies["dotenv"]
mysql = dependencies["mysql"]
dotenv_path = dependencies["dotenv_path"]
db_host = dependencies["db_host"]
db_user = dependencies["db_user"]
db_password = dependencies["db_password"]
db_name = dependencies["db_name"]
    # In this section, you are importing necessary modules and environment variables from the utils module using the import_dependencies function
    # The dependencies dictionary contains imported modules and environment variables
    # This approach makes it easier to manage imports and environment variables in your script




# Example usage
if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv(dotenv_path)

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
    if insert_recipe(recipe_name, instructions, selected_category):
        print("Recipe successfully inserted into the database!")
    else:
        print("Failed to insert the recipe.")
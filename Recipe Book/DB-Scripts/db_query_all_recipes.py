import sqlite3

def query_all_recipes():
    # Connect to the database
    db_connection = sqlite3.connect(r"S:\Python\Recipe Book\Data\recipe_database.db")

    # Create a cursor
    cursor = db_connection.cursor()

    # Define the SQL query to retrieve all recipes
    query = "SELECT * FROM recipes;"

    # Execute the query
    cursor.execute(query)

    # Fetch all the results
    recipes = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()
    db_connection.close()

    return recipes

# Call the function to retrieve all recipes
all_recipes = query_all_recipes()

# Display the results
for recipe in all_recipes:
    print("Recipe ID:", recipe[0])
    print("Name:", recipe[1])
    print("Ingredients:", recipe[2])
    print("Instructions:", recipe[3])
    print("\n")
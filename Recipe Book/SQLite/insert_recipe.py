import sqlite3 

print("starting script...")

def add_recipe(name, ingredients, instructions):
    try:
        # Connect to DB
        db_connection = sqlite3.connect(r"S:\Python\Recipe Book\Data\recipe_database.db")
        
        # Create a cursor
        cursor = db_connection.cursor()
        
        # Define the SQL query for inserting a new recipe
        insert_query = """
        INSERT INTO recipes (name, ingredients, instructions)
        VALUES (?, ?, ?);
        """
        
        # Execute the insert query with the recipe data
        cursor.execute(insert_query, (name, ingredients, instructions))
        
        # Commit the changes
        db_connection.commit()
        
        print("Recipe added successfully!")
        
    except sqlite3.Error as e:
        print("SQLite error:", e)
        
    finally:
        # Close the connection
        db_connection.close()
        print("Changes committed and db connection closed")

# Example usage
recipe_name = "Example Recipe"
recipe_ingredients = "Ingredient 1, Ingredient 2"
recipe_instructions = "Step 1: Do this, Step 2: Do that"

add_recipe(recipe_name, recipe_ingredients, recipe_instructions)
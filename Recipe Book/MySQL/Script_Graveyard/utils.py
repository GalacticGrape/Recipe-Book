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




from utils import import_dependencies, get_categories

if __name__ == "__main__":
    # Import necessary modules and retrieve environment variables
    dependencies = import_dependencies()

    # Create a connection to the database
    connection = dependencies["mysql"].connect(
        host=dependencies["db_host"],
        user=dependencies["db_user"],
        password=dependencies["db_password"],
        database=dependencies["db_name"]
    )

    # Get available categories using the get_categories function
    categories = get_categories(connection)

    # Print the available categories
    print("Available categories:")
    for category in categories:
        print(category)

    # Close the database connection
    connection.close()
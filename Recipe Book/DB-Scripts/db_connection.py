import sqlite3
print("Starting the script...")
def get_db_connection ():
    return sqlite3.connect(r"S:\Python\Recipe Book\Data\recipe_database.db")
connection = get_db_connection()
print("Database connection:", connection) 
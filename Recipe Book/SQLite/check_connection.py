import sqlite3

# Check connection status
def check_connection_status(db_path):
    try:
        db_connection = sqlite3.connect(db_path)
        print("Database connection is open.")
        db_connection.close()
    except sqlite3.Error as e:
        print("Error:", e)

# Specify the path to the SQLite DLL file
dll_path = "S:\Python\Recipe Book\sqlite3.dll"

# Specify the path to the SQLite database file
db_path = r"S:\Python\Recipe Book\Data\recipe_database.db"

# Call the function to check the connection status
check_connection_status(db_path)
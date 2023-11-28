# module_imports.py

import os
from dotenv import load_dotenv
import mysql.connector

def import_database_modules():
    """
    Import necessary modules and retrieve environment variables from .env file.

    Returns:
    dict: A dictionary containing imported modules and environment variables.
    """
    # Specify the path to the .env file
    dotenv_path = r"S:\Python\.env"
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Retrieve environment variables
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    
    # Return the imported modules and variables as a dictionary
    return {
        "os": os,
        "load_dotenv": load_dotenv,
        "mysql": mysql.connector,
        "dotenv_path": dotenv_path,
        "db_host": db_host,
        "db_user": db_user,
        "db_password": db_password,
        "db_name": db_name
    }
# Import libraries
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get database credentials from environment variables
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Create a connection string
connection_string = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

# Read the Excel file
xls = pd.ExcelFile('Sales Data.xlsx')

# Loop through each sheet in the Excel file
for sheet_name in xls.sheet_names:
    # Read the sheet into a DataFrame
    df = pd.read_excel(xls, sheet_name=sheet_name)
    
    # Define the table name
    table_name = sheet_name  

    # Save DataFrame to PostgreSQL
    df.to_sql(table_name, engine, if_exists='replace', index=False)

    print(f"Data from {sheet_name} saved to {table_name} in PostgreSQL database {DB_NAME}")
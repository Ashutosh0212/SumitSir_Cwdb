import requests
import psycopg2
from datetime import datetime, timedelta
import json

# Define the target IP address and endpoint
target_ip = '192.168.1.57:5000'
endpoint = '/get_backup'

# Construct the URL to retrieve backup files
url = f'http://{target_ip}{endpoint}'

# Retrieve backup files from the endpoint
response = requests.get(url)
backup_data = response.json()

# Define your PostgreSQL database connection parameters
db_params = {
    'dbname': 'your_database',
    'user': 'your_user',
    'password': 'your_password',
    'host': 'localhost'
}

# Function to insert backup data into PostgreSQL
def insert_backup_data(data, db_params):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    try:
        for model_data in data:
            model_name = model_data['model']
            for instance_data in model_data['instances']:
                fields = instance_data['fields']
                columns = ', '.join(fields.keys())
                values = [val if not isinstance(val, dict) else json.dumps(val) for val in fields.values()]
                placeholders = ', '.join(['%s' for _ in fields.values()])
                query = f"INSERT INTO {model_name} ({columns}) VALUES ({placeholders})"
                cursor.execute(query, values)

        conn.commit()
        print("Backup data inserted successfully into PostgreSQL.")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting backup data into PostgreSQL:", e)
    finally:
        cursor.close()
        conn.close()

# Insert the retrieved backup data into PostgreSQL
insert_backup_data(backup_data, db_params)

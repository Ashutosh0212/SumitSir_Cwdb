import os
import json
from django.apps import apps
from django.core.management import call_command

def load_backup(backup_file_path):
    try:
        # Check if the backup file exists
        if not os.path.exists(backup_file_path):
            raise FileNotFoundError(f"Backup file '{backup_file_path}' not found.")

        # Load backup data from the JSON file
        with open(backup_file_path, 'r') as f:
            backup_data = json.load(f)

        # Loop through each model data in the backup
        for model_name, model_data in backup_data.items():
            # Get the model class
            model_class = apps.get_model(app_label=model_data[0]['model'])

            # Deserialize the model data and save it to the database
            for obj_data in model_data:
                obj = model_class(**obj_data['fields'])
                obj.save()

        print("Backup data successfully loaded.")

    except Exception as e:
        # Handle exceptions
        raise RuntimeError(f'Error loading backup: {str(e)}')

def display_as_table():
    # Display the data as a table
    call_command('dumpdata')

# Example usage:
backup_file_path = "./backup/whole backup/backup_2024-04-15_10-48-12.json"
load_backup(backup_file_path)
display_as_table()

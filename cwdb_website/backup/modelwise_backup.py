# backup_data.py
import os
import django
import json
from django.apps import apps
from django.core.serializers import serialize

def backup_data():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", r"C:\Users\hp\Desktop\CWDB\cwdb_website\src\settings.py")  # Path to your settings module
    django.setup()

    backup = {}

    # print(apps.get_models())

    # # Iterate over all registered models
    for model in apps.get_models():
        print(model)
    #     model_name = model._meta.model_name
    #     queryset = model.objects.all()
    #     data = json.loads(serialize('json', queryset))
    #     backup[model_name] = data

    # with open('backup.json', 'w') as f:
    #     json.dump(backup, f)

if __name__ == "__main__":
    backup_data()

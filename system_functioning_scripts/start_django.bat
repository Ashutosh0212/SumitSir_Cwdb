batch
   @echo off
   cd D:\IITJodhpur\MTP\CWDB\cwdb_website
   call venv\Scripts\activate
   python manage.py makemigrations
   python manage.py migrate
   start python manage.py runserver 0.0.0.0:8000

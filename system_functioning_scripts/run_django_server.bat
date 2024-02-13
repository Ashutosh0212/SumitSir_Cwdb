@echo off
cd C:\Users\hp\Desktop\CWDB\cwdb_website

echo Running migrations...
python manage.py makemigrations
python manage.py migrate

echo Starting Django development server...
start /B python manage.py runserver 0.0.0.0:8000

:check_loop
timeout /t 5 /nobreak >nul
tasklist /fi "imagename eq python.exe" | find "python.exe" >nul
if errorlevel 1 (
    echo Django development server has crashed. Restarting...
    
    echo %DATE% %TIME% - Server crashed >> server_crash_log.txt
    
    echo Running migrations...
    python manage.py makemigrations
    python manage.py migrate
    
    echo Starting Django development server...
    start /B python manage.py runserver 0.0.0.0:8000
)

goto check_loop

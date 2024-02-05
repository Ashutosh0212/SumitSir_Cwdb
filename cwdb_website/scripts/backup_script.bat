@echo off

set /p password=Enter password: 

rem Check if the entered password matches the expected password
if "%password%"=="Cwdb_MIS_valkyron_77" (
    call C:\path\to\your\virtualenv\Scripts\activate
    python C:\path\to\your\manage.py backup_data
) else (
    echo Incorrect password. Backup operation aborted.
)

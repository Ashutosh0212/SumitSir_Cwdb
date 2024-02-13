@echo off

rem Check if the number of arguments is less than 1
if "%~1"=="" (
    echo Error: Password argument is missing.
    exit /b 1
)

rem Set the password from the first argument
set password=%~1

rem Check if the entered password matches the expected password
if "%password%"=="Cwdb_MIS_valkyron_77" (
    call C:\path\to\your\virtualenv\Scripts\activate
    python C:\path\to\your\manage.py backup_data
) else (
    echo Incorrect password. Backup operation aborted.
    exit /b 1
)

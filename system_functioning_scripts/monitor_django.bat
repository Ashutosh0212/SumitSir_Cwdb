batch
   @echo off
   :start
   timeout /t 300 /nobreak
   powershell -command "& { $status = Invoke-WebRequest http://localhost:8000 -UseBasicParsing; if ($status.StatusCode -ne 200) { Stop-Process -Name python -Force -ErrorAction SilentlyContinue; Start-Process python -ArgumentList 'manage.py runserver 0.0.0.0:8000' -NoNewWindow } }"
   goto start

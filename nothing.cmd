@echo off
echo "Waiting for a few seconds..."
ping 127.0.0.1 -n 5 > nul
cd /d "%~dp0"
python pullusb.py
pause

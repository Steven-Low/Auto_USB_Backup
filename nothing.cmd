echo "Waiting for a few seconds..."
ping 127.0.0.1 -n 5 > nul
python C:\soft\services\Auto_USB_Backup\pullusb.py
pause

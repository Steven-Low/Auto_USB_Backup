REM Get the directory of the batch script
set "script_dir=%~dp0"
REM Create a basic task named "DriverFrameworks Task"

schtasks /create /tn "AutoUSBBackup2" /sc onevent /ec "Microsoft-Windows-DriverFrameworks-UserMode/Operational" /mo "*[System/EventID=2101]" /tr %script_dir%executepy.cmd 
echo Task "AutoUSBbackup2" created successfully.

# Auto_USB_Backup
Tired of dragging and drop from a drive to another? Here come the solution!
Auto_USB_Backup is a program that automate download of files into usb drive when triggered by usb insertion.

# Installation
- Open event viewer and goto application and service log
- Locate Microsoft > Windows > DriverFrameworks-UserMode & Enable the Operational
  
- Open task scheduler on Windows and create a new basic task
- In the Log section, select the Microsoft-Windows-DriverFrameworks-UserMode
- In the EventID, type 2101
- For the action, select start a program and specify the path of nothing.cmd


- Finally, modify the pullusb.py file to save your preference
- Please ensure all python modules are installed.


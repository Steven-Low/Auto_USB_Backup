import os
import shutil
import re
import subprocess
from typing import List, Dict, Optional

'''
# ITERATE THROUGH EACH MOUNTING DISK TO FIND THE VOLUME LABEL
For /F "Delims=\ " %G In ('"%__AppDir__%mountvol.exe 2>NUL|%__AppDir__%find.exe ":\""') Do @Vol %G 2>NUL|%__AppDir__%find.exe /I "VOID">NUL&&CD /D %G

# ITERATE THROUGH EACH POSSIBLE DRIVE LETTER TO FIND THE VOLUME LABEL
For %G In (A B C D E F G H I J K L)Do @Vol %G: 2>NUL|%__AppDir__%find.exe /I "volumelabel">NUL&&CD /D %G:

Credit goes to Compo (Stackoverflow)
'''

def get_drive_info() -> str:
    command = r'''For /F "Delims=\ " %G In ('"%__AppDir__%mountvol.exe 2>NUL|%__AppDir__%find.exe ":\""') Do @Vol %G 2>NUL'''
    output = subprocess.run(command, shell=True, capture_output=True, text=True)
    return output.stdout.strip()

def extract_drive_info(output) -> List[dict]:
    drive_info = []
    pattern = r"Volume in drive ([A-Za-z]) is (.+)"
    matches = re.findall(pattern, output)
    for match in matches:
        drive_info.append({'letter': match[0], 'label': match[1]})
    return drive_info

def get_usb_drive_path(usb_drive_name):
    info = get_drive_info()
    extracted_info = extract_drive_info(info)
    for drive in extracted_info:
        if drive['label'] == usb_drive_name:
            return drive['letter'] + ":\\"  # default to root
    return None

def copy_to_usb(source_folder, usb_drive_name = None, usb_relative_path: Optional[str] = "" ):
    if usb_drive_name:
        usb_drive_path = get_usb_drive_path(usb_drive_name)

    if usb_drive_path:
        # Append relative path to default usb drive path (root)
        usb_drive_path += usb_relative_path
        
        # Recursively copy files from source folder to USB drive
        for root, _, files in os.walk(source_folder):
            for file_name in files:
                source_file = os.path.join(root, file_name)
                relative_path = os.path.relpath(source_file, source_folder)
                destination_file = os.path.join(usb_drive_path, relative_path)


                # Check if destination file already exists
                if not os.path.exists(destination_file):
                    os.makedirs(os.path.dirname(destination_file), exist_ok=True)
                    shutil.copy(source_file, destination_file)
                    print(f"File '{relative_path}' copied to USB drive.")
                # else:
                #     print(f"File '{relative_path}' already exists on USB drive.")
    else:
        print(f"USB drive not found.")

if __name__ == "__main__":

    source_folder = "C:\\Users\\2002l\\Desktop\\Portal" # specify the folder you want to copy recursively to usb
    usb_drive_name = "VOID"          # to identify the volume label and default to usb root for file destination
    usb_relative_path = "Library"  # optional: to specify copy file destination

    copy_to_usb(source_folder, usb_drive_name, usb_relative_path)


   
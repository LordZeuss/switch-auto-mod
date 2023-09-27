import os
import urllib.request
import subprocess
import zipfile
import shutil
import time
import sys

print("Welcome to LordZeus's Switch Mod Utility!")
print(" ")
# Function to display a simple text-based progress bar
def progress_bar(iteration, total, bar_length=50):
    progress = (iteration / total)
    arrow = '=' * int(round(bar_length * progress))
    spaces = ' ' * (bar_length - len(arrow))
    sys.stdout.write(f'\r[{arrow + spaces}] {int(progress * 100)}%')
    sys.stdout.flush()

# Format SD card for switch
# Format SD card for switch
confirmation = input("Do you want to format an SD card? (yes/no): ")

print("\n")
print("Warning: Formatting a drive will erase ALL data on it! Continue at your own risk.")
print("\n")

# Convert the confirmation input to lowercase for case-insensitive comparison
confirmation = confirmation.lower()

if confirmation == 'yes':
    # Get user input for the drive letter
    drive_letter = input("Enter the drive letter to format (e.g., C, D, E): ")

    # Verify that the input is a single letter (e.g., C) and not empty
    if len(drive_letter) == 1 and drive_letter.isalpha():
        # Construct the format command with the /Q option for quick format
        format_command = f"format {drive_letter}: /FS:FAT32 /Q"

        try:
            # Execute the format command
            subprocess.run(format_command, shell=True, check=True)
            print(f"Drive {drive_letter}: quick formatted as FAT32.")
            print("\nDone.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid drive letter input.")
else:
    print("Formatting canceled.")

print("\nStarting necessary downloads...")
print("\n")


## DOWNLOAD TEGRA RCM INSTALLER AND RUN INSTALLER
file_url = 'https://github.com/eliboa/TegraRcmGUI/releases/download/2.6/TegraRcmGUI_v2.6_Installer.msi'
script_directory = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(script_directory, 'TegraRcmGui_Installer.msi')

try:
    urllib.request.urlretrieve(file_url, local_file_path)
    #print(f"File downloaded and saved to {local_file_path}")
    print("Successfully Downloaded TegraRCM Installer")
    print(" ")
except Exception as e:
    print(f"An error occurred: {e}")

# Launch Installer
try:
    if os.path.exists(local_file_path):
        subprocess.Popen([local_file_path], shell=True)
    else:
        print(f"The file '{local_file_path}' does not exist.")
        print(" ")
except Exception as e:
    print(f"An error occurred: {e}")

print(" ")
print(" ")
print("===STOP===")
print("Install TegraRCM via the launched installer, and then click enter to continue.")
print(" ")
input("Press Enter to continue...")
print(" ")
print(" ")

## HEKATE DL
file_url = 'https://github.com/CTCaer/hekate/releases/download/v6.0.6/hekate_ctcaer_6.0.6_Nyx_1.5.5.zip'
script_directory = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(script_directory, 'hekate.zip')

try:
    urllib.request.urlretrieve(file_url, local_file_path)
    ##print(f"File downloaded and saved to {local_file_path}")
    print("Successfully Downloaded Hekate Zip")
    print(" ")
except Exception as e:
    print(f"An error occurred: {e}")

## Sigpatches DL
file_url = 'https://gbatemp.net/attachments/hekate-ams-package3-sigpatches-1-5-5-cfw-16-1-0-zip.389762/'
script_directory = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(script_directory, 'sigpatches.zip')

try:
    urllib.request.urlretrieve(file_url, local_file_path)
    ##print(f"File downloaded and saved to {local_file_path}")
    print("Successfully Downloaded Sigpatches")
    print(" ")
except Exception as e:
    print(f"An error occurred: {e}")

# Unzip for the bin file
zip_file_path = 'hekate.zip'

try:
    if zipfile.is_zipfile(zip_file_path):
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall()
    else:
        print(f"The file '{zip_file_path}' is not a valid ZIP file.")
except Exception as e:
    print(f"An error occurred: {e}")

# Delete extra bootloader file from unzip
folder_to_delete = 'bootloader'
try:
    # Attempt to remove the folder and its contents forcefully
    shutil.rmtree(folder_to_delete, ignore_errors=True)
except Exception as e:
    print(f"An error occurred: {e}")

## DOWNLOAD TEGRA EXPLORER
file_url = 'https://github.com/suchmememanyskill/TegraExplorer/releases/download/4.0.1-hotfix4/TegraExplorer.bin'
script_directory = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(script_directory, 'TegraExplorer.bin')

try:
    urllib.request.urlretrieve(file_url, local_file_path)
    ##print(f"File downloaded and saved to {local_file_path}")
    print("Successfully Downloaded Tegra Explorer")
    print(" ")
except Exception as e:
    print(f"An error occurred: {e}")

## LAUNCH TEGRARCMGUI
tegra_path = "C:\Program Files (x86)\TegraRcmGUI\TegraRcmGUI.exe"

try:
    if os.path.exists(tegra_path):
        subprocess.Popen([tegra_path], shell=True)
    else:
        print(f"The file '{tegra_path}' does not exist. Was it installed?")
except Exception as e:
    print(f"An error occurred: {e}")

## Start sd partition section

# DL emummc
file_url = 'https://nh-server.github.io/switch-guide/files/emummc.txt'
script_directory = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(script_directory, 'emummc.txt')

try:
    urllib.request.urlretrieve(file_url, local_file_path)
    ##print(f"File downloaded and saved to {local_file_path}")
    print("Successfully Downloaded emummc.txt")
    print(" ")

except Exception as e:
    print(f"An error occurred: {e}")

## DL bootlogos
file_url = 'https://nh-server.github.io/switch-guide/files/bootlogos.zip'
script_directory = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(script_directory, 'bootlogos.zip')

try:
    urllib.request.urlretrieve(file_url, local_file_path)
    ##print(f"File downloaded and saved to {local_file_path}")
    print("Successfully Downloaded bootlogos.zip")
    print(" ")
except Exception as e:
    print(f"An error occurred: {e}")

## DL Atmosphere
file_url = 'https://github.com/Atmosphere-NX/Atmosphere/releases/download/1.5.5/atmosphere-1.5.5-master-4fe9a89ab+hbl-2.4.3+hbmenu-3.5.1.zip'
script_directory = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(script_directory, 'atmosphere.zip')

try:
    urllib.request.urlretrieve(file_url, local_file_path)
    #print(f"File downloaded and saved to {local_file_path}")
    print("Successfully Downloaded Atmosphere")
    print(" ")
except Exception as e:
    print(f"An error occurred: {e}")

## DL Lockpick_RCM
file_url = 'https://vps.suchmeme.nl/git/mudkip/Lockpick_RCM/releases/download/v1.9.10/Lockpick_RCM.bin'
script_directory = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(script_directory, 'Lockpick_RCM.bin')

try:
    urllib.request.urlretrieve(file_url, local_file_path)
    #print(f"File downloaded and saved to {local_file_path}")
    print("Successfully Downloaded Lockpick_RCM.bin")
    print(" ")
except Exception as e:
    print(f"An error occurred: {e}")

## DL hekate_ipl.ini
file_url = 'https://nh-server.github.io/switch-guide/files/emu/hekate_ipl.ini'
script_directory = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(script_directory, 'hekate_ipl.ini')

try:
    urllib.request.urlretrieve(file_url, local_file_path)
    #print(f"File downloaded and saved to {local_file_path}")
    print("Successfully Downloaded hekate_ipl.ini")
    print(" ")
except Exception as e:
    print(f"An error occurred: {e}")

## DL JKSV
file_url = 'https://github.com/J-D-K/JKSV/releases/download/02%2F23%2F2023/JKSV.nro'
script_directory = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(script_directory, 'JKSV.nro')

try:
    urllib.request.urlretrieve(file_url, local_file_path)
    #print(f"File downloaded and saved to {local_file_path}")
    print("Successfully Downloaded JKSV.nro")
    print(" ")
except Exception as e:
    print(f"An error occurred: {e}")

## DL ftpd
file_url = 'https://github.com/mtheall/ftpd/releases/download/v3.1.0/ftpd.nro'
script_directory = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(script_directory, 'ftpd.nro')

try:
    urllib.request.urlretrieve(file_url, local_file_path)
    #print(f"File downloaded and saved to {local_file_path}")
    print("Successfully Downloaded ftpd.nro")
    print(" ")
except Exception as e:
    print(f"An error occurred: {e}")

## DL nxthemesinstaller
file_url = 'https://github.com/exelix11/SwitchThemeInjector/releases/download/v-4.7/NXThemesInstaller.nro'
script_directory = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(script_directory, 'NXThemesInstaller.nro')

try:
    urllib.request.urlretrieve(file_url, local_file_path)
    #print(f"File downloaded and saved to {local_file_path}")
    print("Successfully Downloaded NXThemesInstaller.nro")
    print(" ")
except Exception as e:
    print(f"An error occurred: {e}")

## DL NX-Shell
file_url = 'https://github.com/joel16/NX-Shell/releases/download/4.01/NX-Shell.nro'
script_directory = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(script_directory, 'NX-Shell.nro')

try:
    urllib.request.urlretrieve(file_url, local_file_path)
    #print(f"File downloaded and saved to {local_file_path}")
    print("Successfully Downloaded NX-Shell.nro")
    print(" ")
except Exception as e:
    print(f"An error occurred: {e}")

## DL hb-appstore
file_url = 'https://github.com/fortheusers/hb-appstore/releases/download/v2.3.2/appstore.nro'
script_directory = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(script_directory, 'appstore.nro')

try:
    urllib.request.urlretrieve(file_url, local_file_path)
    #print(f"File downloaded and saved to {local_file_path}")
    print("Successfully Downloaded appstore.nro")
    print(" ")
except Exception as e:
    print(f"An error occurred: {e}")

## DL Goldleaf
file_url = 'https://github.com/XorTroll/Goldleaf/releases/download/1.0.0/Goldleaf.nro'
script_directory = os.path.dirname(os.path.abspath(__file__))
local_file_path = os.path.join(script_directory, 'Goldleaf.nro')

try:
    urllib.request.urlretrieve(file_url, local_file_path)
    #print(f"File downloaded and saved to {local_file_path}")
    print("Successfully Downloaded appstore.nro")
    print(" ")
except Exception as e:
    print(f"An error occurred: {e}")

## SETTING UP SD CARD

## Atmosphere extract
print(" ")
print("Starting SD Card configuration...")
print(" ")
drive_letter = input("Enter the drive letter of the formatted switch SD card (e.g., C, D, E): ")

print(" ")

if len(drive_letter) == 1 and drive_letter.isalpha():
    zip_file_name = 'atmosphere.zip' 
    script_directory = os.path.dirname(os.path.abspath(__file__))
    zip_file_path = os.path.join(script_directory, zip_file_name)
    destination_drive = drive_letter + ':\\'
    
    try:
        if os.path.exists(zip_file_path):
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(destination_drive)
            print(f"ZIP file contents extracted to {destination_drive}")
        else:
            print(f"The ZIP file '{zip_file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("Invalid drive letter input. Please enter a single letter (e.g., C, D, E).")

## Hekate extract
zip_file_name = 'hekate.zip'
script_directory = os.path.dirname(os.path.abspath(__file__))
zip_file_path = os.path.join(script_directory, zip_file_name)
destination_drive = drive_letter + ':\\'

try:
    if os.path.exists(zip_file_path):
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(destination_drive)
        print(f"hekate.zip contents extracted to {destination_drive}")
    else:
        print(f"The ZIP file '{zip_file_path}' does not exist.")
except Exception as e:
        print(f"An error occurred: {e}")

## Bootlogos extract
zip_file_name = 'bootlogos.zip'
script_directory = os.path.dirname(os.path.abspath(__file__))
zip_file_path = os.path.join(script_directory, zip_file_name)
destination_drive = drive_letter + ':\\'

try:
    if os.path.exists(zip_file_path):
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(destination_drive)
        print(f"bootlogos.zip contents extracted to {destination_drive}")
    else:
        print(f"The ZIP file '{zip_file_path}' does not exist.")
except Exception as e:
        print(f"An error occurred: {e}")

## Sigpatches extract
zip_file_name = 'sigpatches.zip'
script_directory = os.path.dirname(os.path.abspath(__file__))
zip_file_path = os.path.join(script_directory, zip_file_name)
destination_drive = drive_letter + ':\\'

try:
    if os.path.exists(zip_file_path):
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(destination_drive)
        print(f"'{zip_file_name}' extracted to {destination_drive}")
    else:
        print(f"The ZIP file '{zip_file_name}' does not exist in the script's directory.")
except Exception as e:
    print(f"An error occurred: {e}")

## Copy hekate.ini
file_to_copy = 'hekate_ipl.ini'
script_directory = os.path.dirname(os.path.abspath(__file__))
source_file_path = os.path.join(script_directory, file_to_copy)
destination_directory = os.path.join(drive_letter + ':\\', 'bootloader')

try:
    if os.path.exists(source_file_path):
        os.makedirs(destination_directory, exist_ok=True)

        destination_file_path = os.path.join(destination_directory, file_to_copy)

        shutil.copy2(source_file_path, destination_file_path)

        print(f"File '{file_to_copy}' copied to {destination_directory}")
    else:
        print(f"The file '{file_to_copy}' does not exist in the script's directory.")
except Exception as e:
    print(f"An error occurred: {e}")

## Copy lockpick_rcm.bin
file_to_copy = 'Lockpick_RCM.bin'
script_directory = os.path.dirname(os.path.abspath(__file__))
source_file_path = os.path.join(script_directory, file_to_copy)

destination_directory = os.path.join(drive_letter + ':\\', 'bootloader\\payloads')

try:
    if os.path.exists(source_file_path):
        os.makedirs(destination_directory, exist_ok=True)

        destination_file_path = os.path.join(destination_directory, file_to_copy)

        shutil.copy2(source_file_path, destination_file_path)

        print(f"File '{file_to_copy}' copied to {destination_directory}")
    else:
        print(f"The file '{file_to_copy}' does not exist in the script's directory.")
except Exception as e:
    print(f"An error occurred: {e}")

## Make hosts folder for emummc
directory_path = os.path.join(drive_letter + ':\\', 'atmosphere\\hosts')

try:
    os.makedirs(directory_path, exist_ok=True)
    print(f"Directory '{directory_path}' created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

## Copy emummc.txt to newly created folder
file_to_copy = 'emummc.txt'
script_directory = os.path.dirname(os.path.abspath(__file__))
source_file_path = os.path.join(script_directory, file_to_copy)

destination_directory = os.path.join(drive_letter + ':\\', 'atmosphere\\hosts')

try:
    if os.path.exists(source_file_path):
        os.makedirs(destination_directory, exist_ok=True)

        destination_file_path = os.path.join(destination_directory, file_to_copy)

        shutil.copy2(source_file_path, destination_file_path)

        print(f"File '{file_to_copy}' copied to {destination_directory}")
    else:
        print(f"The file '{file_to_copy}' does not exist in the script's directory.")
except Exception as e:
    print(f"An error occurred: {e}")

## Create appstore folder under switch for appstore.nro
directory_path = os.path.join(drive_letter + ':\\', 'switch\\appstore')

try:
    os.makedirs(directory_path, exist_ok=True)
    print(f"Directory '{directory_path}' created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

## Copy appstore.nro
file_to_copy = 'appstore.nro'
script_directory = os.path.dirname(os.path.abspath(__file__))
source_file_path = os.path.join(script_directory, file_to_copy)

destination_directory = os.path.join(drive_letter + ':\\', 'switch\\appstore')

try:
    if os.path.exists(source_file_path):
        os.makedirs(destination_directory, exist_ok=True)

        destination_file_path = os.path.join(destination_directory, file_to_copy)

        shutil.copy2(source_file_path, destination_file_path)

        print(f"File '{file_to_copy}' copied to {destination_directory}")
    else:
        print(f"The file '{file_to_copy}' does not exist in the script's directory.")
except Exception as e:
    print(f"An error occurred: {e}")

## Copy JKSV.nro
file_to_copy = 'JKSV.nro'
script_directory = os.path.dirname(os.path.abspath(__file__))
source_file_path = os.path.join(script_directory, file_to_copy)
destination_directory = os.path.join(drive_letter + ':\\', 'switch')

try:
    if os.path.exists(source_file_path):
        os.makedirs(destination_directory, exist_ok=True)

        destination_file_path = os.path.join(destination_directory, file_to_copy)

        shutil.copy2(source_file_path, destination_file_path)

        print(f"File '{file_to_copy}' copied to {destination_directory}")
    else:
        print(f"The file '{file_to_copy}' does not exist in the script's directory.")
except Exception as e:
    print(f"An error occurred: {e}")

## Copy ftpd.nro
file_to_copy = 'ftpd.nro'
script_directory = os.path.dirname(os.path.abspath(__file__))
source_file_path = os.path.join(script_directory, file_to_copy)
destination_directory = os.path.join(drive_letter + ':\\', 'switch')

try:
    if os.path.exists(source_file_path):
        os.makedirs(destination_directory, exist_ok=True)

        destination_file_path = os.path.join(destination_directory, file_to_copy)

        shutil.copy2(source_file_path, destination_file_path)

        print(f"File '{file_to_copy}' copied to {destination_directory}")
    else:
        print(f"The file '{file_to_copy}' does not exist in the script's directory.")
except Exception as e:
    print(f"An error occurred: {e}")

## Copy nx-shell.nro
file_to_copy = 'NX-Shell.nro'
script_directory = os.path.dirname(os.path.abspath(__file__))
source_file_path = os.path.join(script_directory, file_to_copy)
destination_directory = os.path.join(drive_letter + ':\\', 'switch')

try:
    if os.path.exists(source_file_path):
        os.makedirs(destination_directory, exist_ok=True)

        destination_file_path = os.path.join(destination_directory, file_to_copy)

        shutil.copy2(source_file_path, destination_file_path)

        print(f"File '{file_to_copy}' copied to {destination_directory}")
    else:
        print(f"The file '{file_to_copy}' does not exist in the script's directory.")
except Exception as e:
    print(f"An error occurred: {e}")

## Copy NxThemesInstaller.nro
file_to_copy = 'NXThemesInstaller.nro'
script_directory = os.path.dirname(os.path.abspath(__file__))
source_file_path = os.path.join(script_directory, file_to_copy)
destination_directory = os.path.join(drive_letter + ':\\', 'switch')

try:
    if os.path.exists(source_file_path):
        os.makedirs(destination_directory, exist_ok=True)

        destination_file_path = os.path.join(destination_directory, file_to_copy)

        shutil.copy2(source_file_path, destination_file_path)

        print(f"File '{file_to_copy}' copied to {destination_directory}")
    else:
        print(f"The file '{file_to_copy}' does not exist in the script's directory.")
except Exception as e:
    print(f"An error occurred: {e}")

## Copy goldleaf.nro
file_to_copy = 'Goldleaf.nro'
script_directory = os.path.dirname(os.path.abspath(__file__))
source_file_path = os.path.join(script_directory, file_to_copy)
destination_directory = os.path.join(drive_letter + ':\\', 'switch')

try:
    if os.path.exists(source_file_path):
        os.makedirs(destination_directory, exist_ok=True)

        destination_file_path = os.path.join(destination_directory, file_to_copy)

        shutil.copy2(source_file_path, destination_file_path)

        print(f"File '{file_to_copy}' copied to {destination_directory}")
    else:
        print(f"The file '{file_to_copy}' does not exist in the script's directory.")
except Exception as e:
    print(f"An error occurred: {e}")

print(" ")
input("Press Enter to Exit")
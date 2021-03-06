
# from datetime import datetime
# import os, sys
# import shutil
# import wmi
# import win32api
# import psutil

# # Listing all the drive letters (win32api)
# drives = win32api.GetLogicalDriveStrings()
# drivers=win32api.GetLogicalDrives
# drives = drives.split('\000')[:-1]
# print(drives)

# c = wmi.WMI()
# for cdrom in c.Win32_CDROMDrive():
#     #print(cdrom.Drive, cdrom.MediaLoaded)
#     if (cdrom.MediaType)=='DVD-ROM':
#         print(cdrom.Drive)

# ############################################################33

import csv
from datetime import datetime
import os
import sys
import shutil
import webbrowser
import wmi
from csv import DictReader

#########################Functions Begin#########################
# Function to copy files from source to destination


def copyfiles(src, dst):
    for item in os.listdir(src):
        source = os.path.join(src, item)
        destination = os.path.join(dst, item)
        if os.path.isdir(source):
            shutil.copytree(source, destination)
        else:
            shutil.copy2(source, destination)

# Function to re-create folder


def recreate_folder(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
        os.makedirs(folder_name)
    else:
        os.makedirs(folder_name)
#########################Functions End#########################


# Creating date and time specific folder
datetime_folder = ((datetime.now()).strftime("%Y/%m/%d/ %H:%M:%S")
                   ).replace("/", "-").replace(":", "-").replace(" ", "")

# Fetching server serial number and server model
os_type = sys.platform.lower()
if "win" in os_type:
    snumber_command = "wmic bios get serialnumber"
    serial_number = os.popen(snumber_command).read().replace(
        "\n", "").replace("	", "").replace(" ", "").replace("SerialNumber", "")

    # Fetching server model
    smodel_command = "wmic computersystem get model"
    server_model = os.popen(smodel_command).read().replace(
        "\n", "").replace("	", "").replace(" ", "").replace("Model", "")

server_model_snumber = '-'.join((server_model, serial_number))
# NEED TO REMOVE THE BELOW COMMENT IN THE FINAL SCRIPT
# tools_path='x:\Windows\Temp\Tools'
tools_path = r'c:\Tools'
dism_src1 = '\\'.join(('C:\dashlog', server_model_snumber))
dism_src = '\\'.join((dism_src1, 'SYSTEM.SAV\CG500IMG'))
# findstr_path = '\\'.join((tools_path, 'findstr6.exe'))
prod_file_path = '\\'.join((tools_path, 'prod.csv'))
input_file_path = '\\'.join((tools_path, 'SKU-List.csv'))
# Need to remove the comment in the final script
# logs_path='\\'.join(('Q:\dashlog\logs',server_model_snumber))
logs_path1 = '\\'.join(('c:\dashlog\logs', server_model_snumber))
logs_path = '-'.join((logs_path1, datetime_folder))

# Creating a System.SAV path
# NEED TO REMOVE IN THE FINAL CODE
recreate_folder(dism_src)

# Creating Logs folder in Dashlog
recreate_folder(logs_path)

# Re-creating Tools folder
recreate_folder(tools_path)

# Copying tools from System.SAV location to RAM disk
copyfiles(dism_src, tools_path)

# Fetching .csv files to Tools path
ECGPATH = os.getcwd()
for files in os.listdir(ECGPATH):
    if files.endswith('.csv'):
        shutil.copy(files, tools_path)


# # Checking for required tools under X:\Windows\Temp\Tools location
# tools_list = [prod_file_path, input_file_path]
# tools_missing_file = '\\'.join((logs_path, 'REQFILEMISSING.TXT'))

# tools_missing = open(tools_missing_file, "w")
# tools_missing.write("Following Tools are missing\n")
# file_count = 0
# for file in tools_list:
#     if os.path.exists(file) == False:
#         tools_missing.write('\n')
#         tools_missing.write(file)
#         tools_missing.write('\n')
#         file_count += 1
# if (file_count != 0):
#     tools_missing.close()
#     webbrowser.open(tools_missing_file)
# else:
#     # if os.path.isfile(tools_missing_file):
#     #     os.remove(tools_missing_file)
#     pass

def tools_missing(tools_list):
    tools_list1=tools_list.split('\n')
    missing_tools_file = '\\'.join((logs_path, 'REQFILEMISSING.TXT'))
    tools_missing = open(missing_tools_file, "w")
    tools_missing.write('Following tool(s) missing')
    tools_missing.write('\n')
    for eachline in tools_list1:
        tools_missing.write(eachline)
        tools_missing.write('\n')
    tools_missing.close()




if os.path.exists(prod_file_path)==False:
    missing_tools_list=prod_file_path
    missing_tools_list+='\n'
if os.path.exists(input_file_path)==False:
    missing_tools_list+=input_file_path
tools_missing(missing_tools_list)

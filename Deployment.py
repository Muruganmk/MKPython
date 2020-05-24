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
# recreate_folder(dism_src)

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

# Checking for required tools under X:\Windows\Temp\Tools location
tools_list = [prod_file_path, input_file_path]
tools_missing_file = '\\'.join((logs_path, 'REQFILEMISSING.TXT'))

tools_missing = open(tools_missing_file, "w")
tools_missing.write("Following Tools are missing\n")
file_count = 0
for file in tools_list:
    if os.path.exists(file) == False:
        tools_missing.write('\n')
        tools_missing.write(file)
        tools_missing.write('\n')
        file_count += 1
if (file_count != 0):
    tools_missing.close()
    webbrowser.open(tools_missing_file)
else:
    # if os.path.isfile(tools_missing_file):
    #     os.remove(tools_missing_file)
    pass

# Checking for drive letter assigned for DVD rom drive
# CALL :DVDLetter
# CALL :Remove-Drv-Letter


# Reading variables from Prod.csv
with open('prod.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:
        prod = row['Prod']
        flav = row['Flav']
        lang = row['Lang']
        ui = row['UI']
        sku = row['SKU']

# Filtering respective SKU for finding image name, drive letter, index number, etc,..
SKU_file = '\\'.join((logs_path, 'SKU.TXT'))
# if os.path.exists(SKU_file):
#         os.remove(SKU_file)
search_string = ','.join(('HPESKU',sku))
searchfile = open("SKU-List.csv", "r")
sku_info = open(SKU_file, "w")
for line in searchfile:
    if search_string in line:
        sku_info.write(line)
searchfile.close()
sku_info.close()

# Reading !SKU!.txt file to get drive letter, Index number, image name, etc..,
fvar=open(SKU_file, 'r')

# read is for storing into a string
data=fvar.read()
fvar.close()
data1=data.split(',')

input_desc=data1[0];input_disk=data1[1]
input_sku=data1[2];input_rev=data1[3]
input_bios=data1[4];input_minipart=data1[5]
input_ospart=data1[6];input_driverpart=data1[7]
input_extra_wim1=data1[8];input_extra_wim2=data1[9]
inpu_extra_wim3=data1[10];input_extra_wim4=data1[11]
inpu_extra_wim5=data1[12];input_extra_wim6=data1[13]
inpu_extra_wim7=data1[14];input_dism=data1[15]



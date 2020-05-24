from datetime import datetime
import os, sys


# Creating date and time specific folder
# datetime_folder=((datetime.now()).strftime("%Y/%m/%d/ %H:%M:%S")).replace("/","-").replace(":","-").replace(" ","")


def datetime_folder():
    current_date=datetime.now()
    split_datetime=current_date.strftime("%Y/%m/%d/ %H:%M:%S")
    datetime_folder=(split_datetime).replace("/","-").replace(":","-").replace(" ","")
    return datetime_folder
def getserial_number():
	os_type = sys.platform.lower()
	if "win" in os_type:
		command = "wmic bios get serialnumber"
	return os.popen(command).read().replace("\n","").replace("	","").replace(" ","").replace("SerialNumber","")

#output machine serial code: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX
print(getserial_number())
print(datetime_folder())

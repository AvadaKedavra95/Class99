import os
import shutil
source=input('Enter the Source Folder Name Here : ')
destination=input('Enter the Destination Folder Name Here : ')
source=source+"/"
destination=destination+'/'
files_list=os.listdir(source)
for files in files_list:
    shutil.copy((source+files),destination)
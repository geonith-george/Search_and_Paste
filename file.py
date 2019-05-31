import os
import shutil,sys
from shutil import copyfile
from os import path
from pathlib import Path, PureWindowsPath

path2=r"C:\Users\User Name\Desktop\Folder1"
dst_dir = r"C:\Users\User Name\Desktop\Folder2"
extension='.txt'
filescopied = 0

try:
    for root, dirs, files in os.walk(path2):
        for file in files: 

            if file.endswith(extension):
                filename = Path(str(file))
                src = path.realpath(str(file))   
                print("filename : ", end='') 
                print(filename)
                print("directory : ", end='')
                copyy=root+"\\"+str(file)
                print(copyy)
                print("destination : ", end='')
                print(dst_dir)
                shutil.copy(copyy, dst_dir)
                filescopied = filescopied + 1
                print(" ")
except Exception as Emove:
    print("Error: ", end='')
    print(Emove) 

print("\nNo of files copied",filescopied)
input("...")


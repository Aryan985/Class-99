import shutil
import os
source = input("Enter the Source: ")
destination = input("Enter the destination: ")
source = source+"/"
destination = destination+"/"
files = os.listdir(source)
for i in files:
    shutil.move((source+i),destination)
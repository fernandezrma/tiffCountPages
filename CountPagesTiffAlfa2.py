# .tiff file multiple images counter.
# Developed by: Miguel Angel Fernandez / fernandezma2@gmail.com
# for Burningham Trucking. https://burninghamtrucking.com/
# License: LGPL ver 2.

import os
from PIL import Image

# Definitions
# count = 0
# Add double "\" to path
tiffs_path = "/home/miguelf/Documents/Burningham/Proyects/BT-scripts/Julio01"
directory = os.fsencode(tiffs_path)

# Screen Conditioning
clear = lambda: os.system('clear')

clear()
print("*****   .tiff Pages Counter   *****")
print()

# Dynamic .tiff directory modification
prompt = input("---> Enter an absolute path to the .tiffs directory or d for default: \n")
if prompt != "d":
    tiffs_path = str(prompt)
#    tiffs_path = tiffs_path.replace('\', '\\')
print()

print("At the folder: " + tiffs_path)
print()

# Operation's directory has to be set to same as target files to be scanned
os.chdir(tiffs_path)

# .tiff operations
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".tif"):
        with Image.open(filename) as img:
            frames = str(img.n_frames)
            print(filename + " has " + frames + " pages")

# Icon Pack XML Generator
# Author : Kunal M.A.

'''

TODO: Add Error handling
    - Check if icon_list.json exists and is not empty
    - Empty `icons` folder
    - Icons in `icon` folder
    - Empty subdirectories in `icons` folder
    - Incorrect file format in `icons` folder
    - Incorrect file format in subdirectories

TODO: Add CLI support for the script
    - Progress messages
    - Error messages

TODO: Ensure Polycon icon is present in the icon pack
    - Check if `polycon.png` is present in the `drawable` folder
    - If not, add it to the `icons` folder via backup
    - Check if `polycon.png` listing is necessary in `drawable.xml`
    - If so, automatically add it to the `drawable.xml` if not present

'''

#######################################
# Initializing essential modules
#######################################

import os
import shutil
import json

# Check if icon_list.json exists
if os.path.exists("scripts/icon_list.json"):
    os.remove("scripts/icon_list.json")

#######################################
# Generate list of icons in text format
#######################################

# Function to get list of files in subdirectories
def folder_list(folders):
    icons = {}
    for folder in folders:
        if os.path.exists("icons/" + folder) and os.path.isdir("icons/" + folder):
            icons[folder] = os.listdir("icons/" + folder)
        else:
            icons[folder] = []
    return icons

# Get list of subdirectories in `icons` folder
subdirs = [f.path for f in os.scandir("icons") if f.is_dir()]
for i in range(len(subdirs)):
    subdirs[i] = subdirs[i].replace("icons\\", "")

# Get list of icons in each subdirectory
icons = folder_list(subdirs)

# Write to icon_list.json
with open("scripts/icon_list.json", "w") as f:
    json.dump(icons, f, indent=4)

# Remove all instances of .png from icon_list.json
with open("scripts/icon_list.json", "r") as f:
    lines = f.readlines()
    with open("scripts/icon_list.json", "w") as f:
        for line in lines:
            f.write(line.replace(".png", ""))

#######################################
# Generate XML files
#######################################

# Read icon_list.json
with open("scripts/icon_list.json", "r") as f:
    icons = json.load(f)

# Making icon_pack.xml
with open("app/src/main/res/values/icon_pack.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="utf-8"?>\n')
    f.write('<resources xmlns:tools="http://schemas.android.com/tools" tools:ignore="ExtraTranslation">\n\n')
    f.write('\t<string-array name="icon_filters">\n')
    for folder, files in icons.items():
        f.write('\t\t<item>' + folder + '</item>\n')
    f.write('\t</string-array>\n\n')
    
    for folder, files in icons.items():
        f.write('\t<string-array name="' + folder + '">\n')
        for file in files:
            f.write('\t\t<item>' + file + '</item>\n')
        f.write('\t</string-array>\n\n')
    f.write('</resources>')

# Making drawable.xml
with open("app/src/main/res/xml/drawable.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="utf-8"?>\n')
    f.write('<resources>\n\n')
    for folder, files in icons.items():
        f.write('\t<category title="' + folder + '" />\n')
        for file in files:
            f.write('\t<item drawable="' + file + '" />\n')
        f.write('\n')
    f.write('</resources>')

# Updating Icon Count in strings.xml
with open("app/src/main/res/values/strings.xml", "r") as f:
    lines = f.readlines()
    with open("app/src/main/res/values/strings.xml", "w") as f:
        for line in lines:
            if "<string name=\"icon_count\">" in line:
                f.write('\t<string name="icon_count">' + str(sum([len(files) for files in icons.values()])) + '</string>\n')
            else:
                f.write(line)

#######################################
# Copy icons to drawable folder
#######################################

for root, dirs, files in os.walk("icons"):
    for file in files:
        if file.endswith(".png"):
            file_path = os.path.join(root, file)
            shutil.copy(file_path, "app/src/main/res/drawable")


#######################################
# Clean up
#######################################

# Remove icon_list.json
os.remove("scripts/icon_list.json")

#######################################
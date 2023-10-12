# 1. place this script in the 3dmigto Mods folder
# 2. specify the toggle key you wish to use on line 18 changing the character before the "\n"
# 3. run the script using 'python toggle_normalization.py'

import os

for root, dirs, files in os.walk("."):
    for file in files:
        if file == "merged.ini":
            path = root + "\\" + file
            print(f"Updating toggle keybind for {path}")

            with open(path, 'r') as file:
                data = file.readlines()

                for i, line in enumerate(data):
                    if line.startswith("key ="):
                        data[i] = "key = p\n"

            with open(path, 'w') as file:
                    file.writelines(data)

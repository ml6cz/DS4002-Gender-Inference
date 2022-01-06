import shutil
import os

basdir = "/Users/megan/Documents/4th Year/DS 4002/Week 1/gender model/crop_images"
newdir = "/Users/megan/Documents/4th Year/DS 4002/Week 1/gender model/Gender"
mapping={"0": "Male", "1": "Female"}
#Make a new folder if the folder does not exist
for key in mapping.keys():
    subfolder = mapping[key]
    dir_path = os.path.join(newdir,subfolder)
    if not os.path.exists(dir_path):
        print(dir_path, "has been created")
        os.makedirs(dir_path)
            
            
for root, dirs, files in os.walk(basdir):
    for filename in files:
        
        #if it is a bad filename (Store is specific to Github)
        if "Store" in filename:
            continue
        old_name = os.path.join(os.path.abspath(root), filename)

        # Separate base from extension
        base, extension = os.path.splitext(filename)
        details = base.split("_")
        
        gender = details[1]
        
        #if it is not one of the values we defined a mapping for
        if gender not in mapping.keys():
            print(gender, " is not a valid value")
            continue
        
        # Initial new name
        new_name = os.path.join(newdir, mapping[gender], base+ extension)
        
        shutil.copy(old_name, new_name)
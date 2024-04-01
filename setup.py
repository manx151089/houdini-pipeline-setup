import shutil
import os

import os
import shutil

def copy_folder_contents(source_dir, dest_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Copy all files from the source directory to the destination directory
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        
        # Skip the file if it already exists in the destination directory
        if os.path.exists(dest_path):
            print('Kill the files if you need to replace the existing file:',dest_path)
            continue
        else:
            shutil.copy(source_path, dest_path)
            print('Sucessfully installed:',dest_path)


# set the paths of the folders you want to copy
packages_path = os.path.join(os.getcwd(), "packages")
houdini_path = os.path.join(os.getcwd(), "houdini-pipeline")

# copy folder2 to the current user's My Documents folder
user_documents = os.path.join(os.path.expanduser("~"), "Documents")

list_of_houdini_folders = [x for x in os.listdir(user_documents) if 'houdini' in x]
for houdini_user_dir in list_of_houdini_folders:
    packages_dest = (os.path.join(user_documents,houdini_user_dir,"packages"))
    copy_folder_contents(packages_path, packages_dest)

tools_dest = copy_folder_contents(packages_path,os.path.join('D:\Tools\houdini'))
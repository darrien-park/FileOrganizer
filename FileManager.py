import os
import shutil
import sys

#TODO: Cover all major file types; shove leftovers in MISC folder
#TODO: Add undo feature
#TODO: Make a GUI
#TODO: Make an option to sort to relevant locations (i.e. Documents, etc)
#TODO: Delete duplicate files
#TODO: Advanced Sort based on content (i.e. tags or keywords)

def create_folders(root, folder_names):
    for x in range(0, 3):
        if not os.path.exists(root + folder_name[x]):
            os.makedirs(root + folder_name[x])


def move_files(list, path, root):
    for files in list:
        if ".dmg" in files:
            os.remove(path + files)
        elif ".app" in files:
            shutil.move(path + files, root + "Applications/" + files)
        elif ".jpg" in files or ".png" in files and not os.path.exists(root + "image/" + files):
            shutil.move(path + files, root + "image/" + files)
        elif ".txt" in files and not os.path.exists(root + "text/" + files):
            shutil.move(path + files, root + "text/" + files)
        elif ".pptx" in files and not os.path.exists(root + "powerpoint/" + files):
            shutil.move(path + files, root + "powerpoint/" + files)
        elif os.path.isdir(path + files):
            new_path = path + files + "/"
            new_names = os.listdir(new_path)
            move_files(new_names, new_path, root)


#list out all the files in the folder

while True:
    try:
        path = input("Enter the directory path: ") + "/"
        if path == "exit/":
            sys.exit()
        names = os.listdir(path)
        break
    except FileNotFoundError:
        print('Not valid directory path! Please try again or type "exit" to quit')

root = path
names = os.listdir(path)
folder_name = ['image','text','powerpoint', 'Applications']

#create new folders
create_folders(root, folder_name)

#move the files into newly created folders based on filename extensions
move_files(names, path, root)

print("Files have been successfully sorted!")


import os
import shutil
import sys

#TODO: Cover all major file types; shove leftovers in MISC folder
#TODO: Add undo feature
#TODO: Make a GUI
#TODO: Make an option to sort to relevant locations (i.e. Documents, etc)
#TODO: Delete duplicate files
#TODO: Advanced Sort based on content (i.e. tags or keywords)

#Create folders for different file types
def create_folders(root, folder_names):
    for x in range(0, len(folder_names)):
        if not os.path.exists(root + folder_name[x]):
            os.makedirs(root + folder_name[x])


def move_files(list, path, root, subdirectory_flag):
    for files in list:
        #Can delete any installers or torrent meta info
        if ".dmg" in files or ".torrent" in files:
            os.remove(path + files)

        elif ".app" in files:
            shutil.move(path + files, root + "Applications/" + files)

        elif ".jpg" in files or ".jpeg" in files or ".png" in files and not os.path.exists(root + "Images/" + files):
            shutil.move(path + files, root + "Images/" + files)

        elif ".mp3" in files or ".wav" in files or ".flac" in files:
            if ".mp3" in files:
                if not os.path.exists(root + 'Music/Compressed'):
                    os.makedirs(root + 'Music/Compressed')
                shutil.move(path + files, root + "Music/Compressed/" + files)
            elif ".flac" in files:
                if not os.path.exists(root + 'Music/Lossless'):
                    os.makedirs(root + 'Music/Lossless')
                shutil.move(path + files, root + "Music/Lossless/" + files)
            else:
                shutil.move(path + files, root + "Music/" + files)

        elif ".txt" in files and not os.path.exists(root + "Text/" + files):
            shutil.move(path + files, root + "Text/" + files)

        elif ".doc" in files or ".docx" in files or ".pdf" in files and not os.path.exists(root + "Documents/" + files):
            if ".pdf" in files:
                if not os.path.exists(root + 'Documents/PDFs'):
                    os.makedirs(root + 'Documents/PDFs')
                shutil.move(path + files, root + "Documents/PDFs/" + files)
            else:
                shutil.move(path + files, root + "Documents/" + files)

        elif ".pptx" in files and not os.path.exists(root + "PowerPoints/" + files):
            shutil.move(path + files, root + "PowerPoints/" + files)

        #if directory then search the directory
        elif os.path.isdir(path + files):
            if subdirectory_flag == 'Y' or subdirectory_flag == 'y':
                if not os.path.exists(root + 'Folders'):
                    os.makedirs(root + 'Folders')
                shutil.move(path + files, root + "Folders/" + files)
            else:
                new_path = path + files + "/"
                new_names = os.listdir(new_path)
                move_files(new_names, new_path, root, subdirectory_flag)

        else:
            shutil.move(path + files, root + "Miscellaneous/" + files)


while True:
    try:
        path = input("Enter the directory path: ") + "/"
        if path == "exit/":
            sys.exit()
        names = os.listdir(path)
        break
    except FileNotFoundError:
        print('Not valid directory path! Please try again or type "exit" to quit')

subdir_flag = None
while True:
    subdir_flag = input("Would you like to move entire sub-folders? (Y/N): ")
    if subdir_flag == 'Y' or subdir_flag == 'y' or subdir_flag == 'N' or subdir_flag == 'n':
        break
    else:
        print("Please enter proper inputs. Ex. 'Y' or 'N'.")

root = path
names = os.listdir(path)
folder_name = ['Images', 'Music', 'Videos', 'Text', 'Documents', 'PowerPoints', 'Applications', 'Miscellaneous']

#create new folders
create_folders(root, folder_name)

#move the files into newly created folders based on filename extensions
move_files(names, path, root, subdir_flag)

print("Files have been successfully sorted!")
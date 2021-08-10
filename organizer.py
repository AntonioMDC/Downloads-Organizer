import os
import shutil
import CONSTANTS


downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')


def create_folders():
    for folder_name in CONSTANTS.FILE_TYPE:
        if not os.path.isdir(os.path.join(downloads_folder, folder_name)):
            os.makedirs(os.path.join(downloads_folder, folder_name))


def search_type(extension):
    folder_name = ""
    known_extension = False
    for file_type in CONSTANTS.FILE_TYPE:
        if extension in CONSTANTS.FILE_TYPE[file_type]:
            known_extension = True
            folder_name = file_type
    return folder_name, known_extension

def move_files():
    duplicates = False
    for filename in os.listdir(downloads_folder):
        folder_name, known_extension= search_type(os.path.splitext(filename)[1])
        if known_extension: 
            try:
                shutil.move(os.path.join(downloads_folder,filename), os.path.join(downloads_folder, folder_name))
            except:
                duplicates = True

    return duplicates   
            

def main():
    create_folders()
    duplicates = move_files()
    if duplicates:
        print("Found duplicates in folders")


if __name__ == "__main__":
    main()
